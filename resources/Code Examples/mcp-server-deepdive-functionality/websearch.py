from mcp.server.fastmcp import FastMCP
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variable
YOUR_API_KEY = os.getenv("YOUR_API_KEY")

mcp = FastMCP("Web Search")

@mcp.tool()
def perform_websearch(query: str) -> str:
    """
    Performs a web search for a query
    Args:
        query: the query to web search.
    """
    messages = [
        {
            "role": "system",
            "content": "You are an AI assistant that searches the web and responds to questions",
        },
        {
            "role": "user",
            "content": query,
        },
    ]

    client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

    response = client.chat.completions.create(
        model="sonar-pro",
        messages=messages,
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    mcp.run()