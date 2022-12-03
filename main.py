import requests
import random
from random import seed, randint
import time
import string
from datetime import datetime
username = str(input("Username: "))
phrase = str(input("Text to Send: "))
seed = 1
counter = 1

def do_requests(username, phrase, seed, counter):
    url = "https://ngl.link/" + username
    while True:
        data = {
            "deviceid": "f69dd341-7n93-4d16-" + str(randint(0, 9999)) + "-" + str(randint(0, 999999999999)),
            "question": str(phrase)}
        r = requests.post(url, json=data)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"Text Sent; requests n: {counter} | {current_time}")
        counter = counter + 1

do_requests(username, phrase, seed, counter)
esc=input("")


