import asyncio
import os
from dotenv import load_dotenv
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=api_key,
    client_options={"api_endpoint": "generativelanguage.googleapis.com"}
)

stdio_server_param = StdioServerParameters(
    command="python",
    args=["C:/Users/matan/projects/mcp_project/mcp_server1/math_server.py"],
)
async def main():
    print("Hello from mcp-server1!")


if __name__ == "__main__":
    asyncio.run(main())
