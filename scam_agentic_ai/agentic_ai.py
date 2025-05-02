from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
import os
import json
from agno.tools.googlesearch import GoogleSearchTools

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# currently our knowlegde base is json for simplicity.
# getting the scam data from the json file
with open("scam_agentic_ai/scam_data.json", "r") as f:
    scams_data = json.load(f)  # scams_data is deserialized into a list.


def get_scam_info(query):
    for scam in scams_data:
        if scam["query"].lower() in query.lower():
            return scam["response"]
    return GoogleSearchTools(query)


scam_awareness_agent = Agent(
    name="Scam Awareness Agent",
    model=Groq(id="deepseek-r1-distill-llama-70b", api_key=GROQ_API_KEY),
    tools=[get_scam_info],
    description="A WhatsApp chatbot that educates Indian users about digital scams like UPI fraud and phishing, offering advice to stay safe and preventive measures they can take.",
    instructions=[
        "you are a scam awareness bot for India.",
        "Answer queries about digital scams using the provided knowledge base.",
        "Keep replies short, clear, and empathetic,actionable.",
        "Suggest calling 1930 or visiting cybercrime.gov.in when relevant.",
    ],
    show_tool_calls=True,
    markdown=True,
)

if __name__ == "__main__":
    # useage: agent.print_response("Your query here")
    scam_awareness_agent.print_response(
        "what does digital arrest mean and how can we prevent that from scamming me?",
        stream=True,
    )
