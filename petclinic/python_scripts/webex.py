import requests
import os

WBX_KEY = os.getenv("WBX_KEY")
WBX_ROOM_ID = os.getenv("WBX_ROOM_ID")
MESSAGE = os.getenv("MESSAGE")

WEBEX_API = "https://api.ciscospark.com/v1/"
# print(WBX_KEY)
# print(WBX_ROOM_ID)
# print(MESSAGE)


webex_session = requests.Session()
webex_headers = {"Authorization": "Bearer " + WBX_KEY}
webex_session.headers.update(webex_headers)

webex_message_json = {
    "roomId": WBX_ROOM_ID,
    "text": MESSAGE
}
webex_message = webex_session.post(url=WEBEX_API + "messages", json=webex_message_json)
print(webex_message)
#print(webex_message.json())
