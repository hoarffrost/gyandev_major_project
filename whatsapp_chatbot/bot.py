"""import sys
import os

# Get the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from flask import Flask, request, jsonify
import requests

from scam_agentic_ai.agentic_ai import (
    scam_awareness_agent,
)  # Import the agent from agentic_ai.py


app = Flask(__name__)

# Replace with your WhatsApp Business Cloud API credentials
ACCESS_TOKEN = "EAAJXpQNNo8YBOwwQhCMQiVk8BBmnYTK34JU4zM3BKKjdrXDfbt5b66r1WCtuETytpXiZCbyy3lwgbvTp64TYSdCeoPTbZAoelFBaywOCOTmHh04TsNmm5JHkzktwGm2yd73PO9BE66cHklE0UfQSh5ZAt32xhBotbYLcg6KLdZB7aKZASp1nCEYQDIU0K51ocXPwbHB717YSYsL92ZAMDeMu7OZB9MZD"
PHONE_NUMBER_ID = "678267122029578"
API_URL = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if data and "messages" in data["entry"][0]["changes"][0]["value"]:
        messages = data["entry"][0]["changes"][0]["value"]["messages"]
        for message in messages:
            if "text" in message:
                sender_id = message["from"]
                user_query = message["text"]["body"]

                # Use the agent to get a response
                # agent_response = scam_awareness_agent.get_response(user_query)

                agent_response = "Hello! This is a placeholder response from the agent."

                # Send the agent's response back to the user
                send_message(sender_id, agent_response)
    return jsonify({"status": "received"}), 200


# meta cloud api, will send the request to fetch the hub.verify_token i have given there.
@app.route("/webhook", methods=["GET"])
def verify():
    VERIFY_TOKEN = "12345"
    if (
        request.args.get("hub.mode") == "subscribe"
        and request.args.get("hub.verify_token") == VERIFY_TOKEN
    ):
        return request.args.get("hub.challenge"), 200
    return "Verification failed", 403


@app.route("/")
def landing():
    return (
        "<h1>WhatsApp Chatbot</h1><p>This is a simple WhatsApp chatbot using Flask.</p>"
    )


def send_message(recipient_id, message_text):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": recipient_id,
        "text": {"body": message_text},
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


if __name__ == "__main__":
    app.run(port=8000, debug=True)
"""

from pywa import WhatsApp, filters, types
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

SYSTEM_USER_ACCESS_TOKEN = os.getenv("SYSTEM_USER_ACCESS_TOKEN")
APP_SECRET = os.getenv("APP_SECRET")

# whatsapp client
wa = WhatsApp(
    phone_id="678267122029578",
    token=SYSTEM_USER_ACCESS_TOKEN,
    server=app,
    callback_url="https://digitalscamawarenessagenticai.vercel.app",
    verify_token="12345",
    app_id=659316190061510,
    app_secret=APP_SECRET,
)


@wa.on_message(filters.text)
def new_message(_: WhatsApp, msg: types.Message):
    msg.reply("Hello from PyWa!")
