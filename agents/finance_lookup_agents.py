from dotenv import load_dotenv

load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate

from langchain_core.tools import Tool


def lookup(name: str) -> str:
    return 'https://finance.yahoo.com/news/heres-1-stock-warren-buffett-202200602.html'

`