import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def get_llm(model="gpt-4", temperature=0.3):
    return ChatOpenAI(
        model=model,
        temperature=temperature,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )