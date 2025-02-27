from langchain_community.tools.tavily_search import TavilySearchResults
import os

from dotenv import load_dotenv

os.environ["TAVILY_API_KEY"]  = os.getenv("TAVILY_API_KEY")

tools = [TavilySearchResults(max_results=1)]