from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
import os
from agno.tools.googlesearch import GoogleSearchTools

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

scam_awareness_agent = Agent(
    name="Scam Awareness Agent",
    model=Groq(id="llama-3.3-70b-versatile", api_key=GROQ_API_KEY),
    tools=[GoogleSearchTools()],
    description="You are a digital scam awareness and prevention agent that helps users find the latest news about the digital scam happening in India and how to prevent them.",
    instructions=[
        "Provide the quick actionable steps taken to prevent the scam or report it.",
        "Include only on Indian news.",
        "Search for 10 news items and select the top 4 unique items.",
    ],
    show_tool_calls=True,
    markdown=True,
)

scam_awareness_agent.print_response(
    "Provide important official phone numbers and websites and contact information in case of scam or prevention.",
    stream=True,
)
