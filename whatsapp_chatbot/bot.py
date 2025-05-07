from pywa import WhatsApp, filters, types
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from dotenv import load_dotenv
from agno.agent import RunResponse
import os, sys, json

# Get the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from scam_agentic_ai.agentic_ai import (
    scam_awareness_agent,
)  # Import the agent from agentic_ai.py

load_dotenv()

fastapi_app = FastAPI()

SYSTEM_USER_ACCESS_TOKEN = os.getenv("SYSTEM_USER_ACCESS_TOKEN")
APP_SECRET = os.getenv("APP_SECRET")

# whatsapp client
wa = WhatsApp(
    phone_id="678267122029578",
    token=SYSTEM_USER_ACCESS_TOKEN,
    server=fastapi_app,
    callback_url="https://d3ddb8f8a4d8283faea35c7dd0afac41.serveo.net",
    verify_token="12345",
    app_id=659316190061510,
    app_secret=APP_SECRET,
)

WELCOME_MESSAGE = """Hello! 👋 I'm ScamSafeBot, here to help you stay safe from digital scams.

I can provide information about common scams in India and how to protect yourself.

Try asking me about:
- UPI scams
- Phishing attacks
- Digital arrest scams
- Investment fraud
- Or any other scam you're concerned about

Need immediate help? Call 1930 or visit cybercrime.gov.in
"""

user_sessions = {}


@wa.on_message(filters.text)
def handle_message(client: WhatsApp, msg: types.Message):
    user_id = (
        msg.from_user.wa_id
    )  # not the phone id of client rather the number with country code.
    user_query = msg.text

    # Add typing indicator
    client.indicate_typing(msg.id)

    # Initialize user session if first message
    if user_id not in user_sessions:
        user_sessions[user_id] = {"is_first_message": True}

    # Send welcome message for first-time users
    if user_sessions[user_id].get("is_first_message", False):
        user_sessions[user_id]["is_first_message"] = False
        client.send_message(user_id, WELCOME_MESSAGE)
        client.indicate_typing(msg.id)  # Resume typing for main response

    try:
        # user session id
        session_id = f"session_{user_id}"
        # Process the user query with the scam awareness agent
        response: RunResponse = scam_awareness_agent.run(
            user_query, session_id=session_id, user_id=user_id
        ).to_json()

        respose_json_serialized = json.loads(
            response
        )  # Deserialize the JSON string into a Python dictionary

        # Send the response
        client.send_message(user_id, respose_json_serialized["content"])

        # If this is their first topic-specific query, show the menu
        # if user_sessions[user_id].get("show_menu", True):
        #     user_sessions[user_id]["show_menu"] = False
        #     send_menu(client, user_id)

    except Exception as e:
        error_msg = (
            "Sorry, I'm having trouble processing your request. Please try again later."
        )
        client.send_message(user_id, error_msg)
        print(f"Error processing message: {e}")
