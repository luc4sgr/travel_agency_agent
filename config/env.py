import os
from dotenv import load_dotenv

def load_environment():
    load_dotenv()
    return {
        "GROQ_API_KEY": os.getenv("GROQ_API_KEY"),
        "SERPER_API_KEY": os.getenv("SERPER_API_KEY"),
    }
