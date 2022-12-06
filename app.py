import time
import requests
from flask import Flask
from threading import Thread
import os
 
TOKEN = ""   #token  
channel_id = "" #channel_id
 
count = 0
url = f"https://discord.com/api/v9/channels/{channel_id}/typing"
headers = {
  'authorization': TOKEN
}
 
app = Flask('')
 
@app.route('/')
def home():
	return ("Bot is up to run")
 
def run():
  app.run(
		host='0.0.0.0',
		port=8080
	)
 
def update():
	t = Thread(target=run)
	t.start()
 
update()
while True:
	response = requests.request("POST", url, headers=headers)
	if response.status_code != 204:
		print(f"Failed:{response.text}")
	else:
		count += 1
		print(f"Sent packets: {count}")
	time.sleep(8) #in seconds