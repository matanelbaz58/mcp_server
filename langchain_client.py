import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")


llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest", google_api_key=os.getenv("GOOGLE_API_KEY")
)


async def main():
    async with MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [
                    "C:/Users/matan/projects/mcp_project/mcp_server1/math_server.py"
                ],
            },
            "weather": {
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            },
        }
    ) as client:
        agent = create_react_agent(llm, client.get_tools())
        result = await agent.ainvoke({"messages":"what is the weather in tel aviv?"})
        print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
