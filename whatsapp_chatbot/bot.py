import sys
import os

# Get the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from scam_agentic_ai.agentic_ai import (
    scam_awareness_agent,
)  # Import the agent from agentic_ai.py

from pywa import WhatsApp, filters, types
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

fastapi_app = FastAPI()

SYSTEM_USER_ACCESS_TOKEN = os.getenv("SYSTEM_USER_ACCESS_TOKEN")
APP_SECRET = os.getenv("APP_SECRET")

# whatsapp client
wa = WhatsApp(
    phone_id="678267122029578",
    token=SYSTEM_USER_ACCESS_TOKEN,
    server=fastapi_app,
    callback_url="",
    verify_token="12345",
    app_id=659316190061510,
    app_secret=APP_SECRET,
)


@wa.on_message(filters.text)
def new_message(_: WhatsApp, msg: types.Message):
    msg.reply("Hello from PyWa!")
