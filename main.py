## IMPORTS

import requests
import time
import json
from discord_webhook import DiscordWebhook

spamCount = 0
inputWebhook = input("Please enter a valid Discord webhook: ")

## VARIABLES

webhookReq = requests.get(inputWebhook, headers={"name": "application/json"})
json = json.loads(webhookReq.text)

## WEBHOOK CHECK

if json == {'message': 'Invalid Webhook Token', 'code': 50027}:
    print("Webhook was found invalid! Exiting in 5 seconds...")
    time.sleep(5)

    print("Exiting now.")
    exit()

spamMessage = input("Please enter your desired Spam Message: ")

## WEBHOOK INFO

print("WEBHOOK INFO")
print("WEBHOOK ID: " + json["id"])
print("WEBHOOK NAME: " + json["name"])
print("WEBHOOK TOKEN: " + json["token"])
print("WEBHOOK CHANNEL ID: " + json["channel_id"])
print("WEBHOOK GUILD ID: " + json["guild_id"])

webhook = DiscordWebhook(url=inputWebhook, rate_limit_retry=True, content=spamMessage)

while True:
    if webhook:
        webhook.execute()
        spamCount += 1
        
        print(f"Successfully sent webhook with {spamMessage}! Spam Count: {spamCount}")