# -*- coding: utf-8 -*-

import time
import os
import random

from rocketchat_py_sdk.driver import Driver

bot_username = os.getenv('BOT_USERNAME', 'bot_rasa')
bot_password = os.getenv('BOT_PASSWORD', 'bot_rasa')
rocket_url = os.getenv('ROCKET_URL', 'localhost:3000')


attachmentDict = {
  "text button with url": [{
      "title": "text button with url",
      "actions": [
        {
          "type": "button",
          "text": "Book flights",
          "url": "http://www.kayak.com",
          "is_webview": False
        }
      ]
    }],
  "text button with msg in chat window":[{
      "title": "text button with msg in chat window",
      "actions": [
        {
          "type": "button",
          "text": "Say hello in chat window?",
          "msg": "hello in chat window",
          "msg_in_chat_window": True
        }
      ]
    }],
  "image button with url":[{
      "title": "image button with url",
      "actions": [
        {
          "type": "button",
          "url": "http://www.kayak.com",
          "image_url": "http://www.emoji.co.uk/files/phantom-open-emojis/travel-places-phantom/12698-airplane.png",
          "is_webview": False
        }
      ]
    }],
  "image button with msg in chat window":[{
      "title": "image button with msg in chat window",
      "actions": [
        {
          "type": "button",
          "image_url": "http://www.emoji.co.uk/files/phantom-open-emojis/travel-places-phantom/12698-airplane.png",
          "msg": "I clicked the airplane",
          "msg_in_chat_window": True
        }
      ]
    }],
  "multiple text buttons":[{
      "title": "multiple text buttons with url",
      "actions": [
        {
          "type": "button",
          "text": "Book flights",
          "url": "http://www.kayak.com",
          "is_webview": False
        },
        {
          "type": "button",
          "text": "Cancel travel request",
          "url": "https://requests.example.com/cancel/r123456",
          "is_webview": False
        }
      ]
    }],
  "horizontal text buttons":[{
      "title": "horizontal text buttons with url",
      "button_alignment": "horizontal",
      "actions": [
        {
          "type": "button",
          "text": "Book flights",
          "url": "http://www.kayak.com",
          "is_webview": False
        },
        {
          "type": "button",
          "text": "Cancel travel request",
          "url": "https://requests.example.com/cancel/r123456",
          "is_webview": False
        }
      ]
    }],
  "attachment with buttons":[{
      "title": "Lauri M(title field)",
      "title_link": "https://www.basketball-reference.com/players/m/markkla01.html",
      "text": "Should have been rookie of the year (text field)",
      "description": "What a great player! (description field)",
      "image_url": "http://www.trbimg.com/img-5b04c449/turbine/ct-spt-bulls-lauri-markkanen-all-rookie-team-20180522",
      "actions": [
        {
          "type": "button",
          "text": "Book flights",
          "url": "https://www.kayak.com",
          "is_webview": False
        },
        {
          "type": "button",
          "text": "Cancel travel request",
          "url": "https://www.kayak.com",
          "is_webview": False
        }
      ]
    }]
}

replyDict = {
  "hello in chat window": "received your ‘hello in chat window’",
  "I clicked the airplane": "received your response about clicking the airplane"
}

def process_message(bot, message):
    text = message['msg']

    if(text in attachmentDict):
      bot.send_attachment(message['rid'], attachmentDict[text])
    elif(text in replyDict):
      bot.send_message(message['rid'], replyDict[text])

def start(bot):
    bot.connect()
    bot.login(user=bot_username, password=bot_password)

    bot.subscribe_to_messages()
    bot.add_prefix_handler('', process_message)

    while True:
        time.sleep(3600)

if __name__ == '__main__':
    start(Driver(url=rocket_url, ssl=False, debug=True))
