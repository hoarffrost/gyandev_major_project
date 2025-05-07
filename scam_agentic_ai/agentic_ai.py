from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
import os
import json
from datetime import datetime
from textwrap import dedent
from agno.tools.exa import ExaTools
from agno.storage.sqlite import SqliteStorage
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
EXA_API_KEY = os.getenv("EXA_API_KEY")


# currently our knowlegde base is json for simplicity.
# getting the scam data from the json file
with open("scam_agentic_ai/scam_data.json", "r") as f:
    scams_data = json.load(f)  # scams_data is deserialized into a list.


# Tool
def get_scam_info(query: str) -> str:
    for scam in scams_data:
        if scam["scam"].lower() in query.lower():
            return json.dumps({"advice": scam["advice"], "example": scam["example"]})
    return json.dumps(
        {
            "advice": "I’m not sure about this scam. It sounds risky—call 1930 or visit cybercrime.gov.in for help.",
            "example": "Scammers often trick people with fake messages. Always verify before acting.",
        }
    )


# Agent
today = datetime.now().strftime("%Y-%m-%d")

# Setup storage and memory
agent_storage = SqliteStorage(
    table_name="agent_sessions", db_file="db/your_db_path.db", auto_upgrade_schema=True
)
memory_db = SqliteMemoryDb(table_name="memory", db_file="db/your_db_path.db")
memory = Memory(db=memory_db)

scam_awareness_agent = Agent(
    name="ScamShield",
    model=Groq(id="llama-3.3-70b-versatile", api_key=GROQ_API_KEY),
    tools=[
        get_scam_info,
        ExaTools(
            start_published_date=today,
            include_domains=["cybercrime.gov.in"],
            type="keyword",
            api_key=EXA_API_KEY,
        ),
    ],
    description=dedent(
        """\
        I am ScamShield, your trusted WhatsApp companion dedicated to protecting Indian users from digital fraud! 🛡️

        My mission is to educate and empower users through:
        - Real-time scam alerts and prevention tips
        - Interactive fraud awareness scenarios
        - Step-by-step guidance for secure digital transactions
        - Verification tools for suspicious links/messages
        - Emergency reporting procedures
        
        I communicate with:
        - Simple, clear language in English and Hindi
        - Relatable real-world examples
        - Visual aids and infographics
        - Quick response templates for common scams
        - Verified safety tips from cybercrime authorities
        
        I specialize in protecting against:
        - UPI payment fraud
        - Phishing attacks
        - KYC scams
        - Job fraud
        - Loan app scams
        - Digital arrest threats
        - Investment schemes
        
        Available 24/7 to help users stay safe in the digital world!
    """
    ),
    instructions=dedent(
        f"""
        Response Format (4000 characters max)
        Your responses should follow this clear structure:

        📱 *What is this scam?*
        [Brief, clear explanation, include exact name of the scam]

        🎭 *How it happens:*
        [Engaging story example from get_scam_info]

        ⚠️ *What to do:*
        [Clear, actionable steps]

        🆘 *Need help?*
        Call 1930 or visit cybercrime.gov.in

        Content Guidelines:
        • Keep responses 100-150 words
        • Use friendly, empathetic language 
        • Include real examples from scam database
        • Add practical safety tips like:
        - "Always verify QR codes in banking app"
        - "Never share OTPs - even with bank staff"
        • Cite trusted Indian sources (RBI, I4C)

        For Urgent Messages:
        🚨 Prioritize immediate action:
        - "Hang up immediately"
        - "Block the number" 
        - "Report to 1930"

        Conversation Management:
        • Remember context from previous messages
        • Reference relevant past interactions
        • Build on established rapport
        • Maintain consistent personality
        • Track user's knowledge level
        • Adapt responses based on history
        • Use memory to personalize advice
        • Follow up on previous concerns
        • Keep engagement friendly but professional

        End each message with:
        💡 "Want more safety tips? You can ask me absolutely anything about digital scams, I'm here to help!"

        Date: {today}
    """
    ),
    markdown=True,
    show_tool_calls=False,
    add_datetime_to_instructions=True,
    storage=agent_storage,
    memory=memory,
    enable_user_memories=True,
    add_history_to_messages=True,
    num_history_runs=3,
)

if __name__ == "__main__":
    # useage: agent.print_response("Your query here")
    scam_awareness_agent.print_response(
        "I got a scam call telling me the he needs to give me 50k as my father told him to. What should I do?",
        stream=True,
    )
