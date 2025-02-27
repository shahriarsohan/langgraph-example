from langchain_community.tools.tavily_search import TavilySearchResults
import os
from dotenv import load_dotenv

# Load environment variables before accessing them
load_dotenv()

# Get the Tavily API key from environment variables
tavily_api_key = os.getenv("TAVILY_API_KEY")
if not tavily_api_key:
    raise ValueError("TAVILY_API_KEY environment variable not set")

os.environ["TAVILY_API_KEY"] = tavily_api_key

# Initialize the tools
tools = [TavilySearchResults(max_results=1)]