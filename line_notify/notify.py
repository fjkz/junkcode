import requests

# get from https://notify-bot.line.me/my/
ACCESS_TOKEN = 'XXXXXXXXXXXXXXXXX'

headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN}
payload = {'message': 'Hello! This is a test message.'}
response = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
print(response)
