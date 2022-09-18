from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os.path
import sys
import schedule
from time import sleep

# TODO: input your personal infomation
NAME = "xxxxxxx"
TEL = ["xxx", "xxxx", "xxxx"]
EMAIL = "xxxxxxx@gmail.com"

# time slot you want to book
TARGET_HOUR = 18

def find_free_and_book(driver):
    page = "https://select-type.com/rsv/?id=0AEeQuFE0HM"
    driver.get(page)
    num_men = driver.find_element(By.ID, "chknum_id")
    num_men.send_keys("1")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # td:nth-child(4): day after tomorrow
    # tr:nth-child(N): target hour. N = H - 11
    selector = "body > div.body > div > div.row-fluid > div > div.content-body > div.cl-type-week.rsvcal_cls > div > table > tbody > tr:nth-child({:d}) > td:nth-child(4) > div > div".format(TARGET_HOUR - 11)
    target_slot = soup.select(selector)[0]
    if target_slot.get_text().strip() == "×":
        print(datetime.now(), "target slot is occupied")
        return False

    driver.find_element(By.CSS_SELECTOR, selector).click()

    wait = WebDriverWait(driver, 5)
    button = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#rsvsltmodal_footer_id > input"))
    )
    button.click() 

    name_slc = "#rsvForm_id > div > div > div > div > div:nth-child(4) > div > div:nth-child(3) > div > input.span5.chg-text2.input_bg_col_cls"
    tel_slc = [
        "#rsvForm_id > div > div > div > div > div:nth-child(4) > div > div:nth-child(4) > div > input:nth-child(1)",
        "#rsvForm_id > div > div > div > div > div:nth-child(4) > div > div:nth-child(4) > div > input:nth-child(2)",
        "#rsvForm_id > div > div > div > div > div:nth-child(4) > div > div:nth-child(4) > div > input:nth-child(3)",
    ]
    email_slc = ["#rsvpif_email_id", "#rsvpif_email_conf_id"]

    slc_value = [
        (name_slc, NAME),
        (tel_slc[0], TEL[0]),
        (tel_slc[1], TEL[1]),
        (tel_slc[2], TEL[2]),
        (email_slc[0], EMAIL),
        (email_slc[1], EMAIL),
    ]
    for slc, value in slc_value:
        elm = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, slc))
        )
        elm.send_keys(value)

    selector = "#rsvForm_id > div > div > div > div > div.content-footer.align-center > input"
    driver.find_element(By.CSS_SELECTOR, selector).click()

    button = wait.until(
        EC.visibility_of_element_located((By.ID, "ebtn_id"))
    )
    button.click()
    print(datetime.now(), "booked!!")
    return True


if __name__ == "__main__":
    # open selenium driver
    driver_path = os.path.join(os.path.dirname(sys.argv[0]), "libexec", "chromedriver.exe")
    driver = webdriver.Chrome(driver_path)

    def onetime_job():
        find_free_and_book(driver)
        return schedule.CancelJob

    # We can book new slots from 00:00 AM every night
    schedule.every().day.at('00:00:01').do(onetime_job)

    while True:
        schedule.run_pending()
        sleep(1)

    driver.quit()
