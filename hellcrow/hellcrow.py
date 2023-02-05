import logging
import os.path
import sys
import time
from datetime import datetime

import requests
import yaml
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

TRIAL_MODE = True
if not TRIAL_MODE:
    print("****************************************")
    print(" CAUTION: Not Trial Mode")
    print("****************************************")
    time.sleep(5)

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
log = logging.getLogger(__name__)

# load config
file_path = os.path.join(os.path.dirname(sys.argv[0]), "config.yml")
with open(file_path, encoding="utf8") as f:
    config = yaml.load(f, Loader=yaml.Loader)
log.info(f"loaded {file_path}: {config}")

site = config["site"]


def login(page):
    page.goto(site["home_url"])
    log.info("page opened: %s", page.title())
    page.locator("a", has_text="ログイン").click()
    log.info("start login")
    page.locator("id=user").fill(site["id"])
    page.locator("id=pass").fill(site["password"])
    page.locator("input", has_text="ログイン").click()
    log.info("wait login completion")
    # check login state
    nickname = site["nickname"]
    log.info(f"login succeeded: %s", page.locator("text=" + nickname).text_content())


def find_free_slot(html):
    soup = BeautifulSoup(html, "html.parser")
    table = soup.select_one("#chart > div > table > tbody")

    if not table:
        log.warn("schedule table is not found")
        return []

    free_slots = {}
    for i, row in enumerate(table.find_all("tr")):
        time_str = row.find("th").get_text()
        for j, cell in enumerate(row.find_all("td")):
            if cell.span and cell.span.get_text() == "○":
                date_str = cell.input["value"]
                atime = datetime.strptime(date_str + "-" + time_str, "%Y-%m-%d-%H:%M-")
                free_slots[atime] = (i, j)
    return free_slots


def line_notify(message):
    headers = {"Authorization": "Bearer " + config["line_token"]}
    payload = {"message": message}
    response = requests.post(
        "https://notify-api.line.me/api/notify", headers=headers, params=payload
    )
    log.info("sent LINE message: %s", response)


def snipe(page, target, retry_sec):
    name = target["name"]
    o_url = target["outer_url"]
    i_url = target["inner_url"]

    log.info("check %s's schedule: %s", name, o_url)
    page.goto(o_url)

    start_time = time.time()
    count = 0
    while time.time() - start_time < retry_sec:
        page.goto(i_url)
        html = page.content()
        free_slots = find_free_slot(html)
        if free_slots:
            break
        log.info(f"{name} has no free slot. try again. {count}")
        count += 1
    else:
        log.error("she is always busy")
        return False

    log.info(f"{name}'s free time: %s", ", ".join(str(slot) for slot in free_slots))

    my_free = config["my_free_time"]
    earliest = datetime.strptime(my_free["earliest_start"], "%Y-%m-%d %H:%M")
    latest = datetime.strptime(my_free["latest_start"], "%Y-%m-%d %H:%M")
    good_slots = [slot for slot in free_slots if earliest <= slot <= latest]
    if not good_slots:
        log.error(f"window [{earliest}, {latest}] is already booked")
        return False
    target_time = sorted(good_slots)[0]

    i, j = free_slots[target_time]
    css_selector = "#chart > div > table > tbody > tr:nth-child({:d}) > td:nth-child({:d}) > span".format(
        i + 1, j + 2
    )
    page.locator(css_selector).click()

    # cource page
    course = target["course"]
    page.locator("input", has_text="選択する").nth(course).click()

    # option page
    # some times no this page. in that case, comment out please.
    options = target['option']
    for op in options:
        page.locator("li", has_text=op).first.click()
    page.locator("button", has_text="確定して次へ").first.click()

    # T&A page
    page.locator("label", has_text="次回から表示しない").uncheck()
    page.locator("button", has_text="次へ").click()

    # my infomation page
    my_info = config["my_info"]
    page.locator("id=customer_name").fill(my_info["name"])
    page.locator("id=reservation_phone_number").fill(my_info["tel"])
    page.locator("id=mail_pc_sp").fill(my_info["email"])
    page.locator("id=customer_input_notes").fill(my_info["comment"])

    checkbox = page.locator("id=contact_from_check")
    if checkbox.is_visible():
        checkbox.check()

    page.locator("a", has_text="確定して次へ").click()

    # submit reserve page
    log.info(page.locator("form", has_text="ご予約内容").text_content())
    # if TRIAL_MODE, it doesn't submit actually
    page.locator("a", has_text="上記に同意の上、ネット予約する").click(trial=TRIAL_MODE)
    log.info(f"reserve {name} at {target_time}")
    line_notify(f"reserve {name} at {target_time}")
    return True


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.set_default_timeout(60000)
    login(page)

    start_time = datetime.strptime(config["job_start"], "%Y-%m-%d %H:%M:%S")
    diff = (start_time - datetime.now()).total_seconds()
    if diff < 0:
        diff = 0
    log.info("sleep until %s, for %s soconds", start_time, diff)
    time.sleep(diff)
    hit = snipe(page, config["target"], config["retry_sec"])
    browser.close()
