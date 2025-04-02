from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI

api_key = open("google_api_key.secret").read().strip()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=api_key)
print("intitalized")


async def main():
    async with MultiServerMCPClient(
        {
            # "math": {
            #     "command": "python",
            #     # Make sure to update to the full absolute path to your math_server.py file
            #     "args": ["math_mcp_server.py"],
            #     "transport": "stdio",
            # },
            "math": {
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            },
        }
    ) as client:
        agent = create_react_agent(model, client.get_tools())
        math_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
        weather_response = await agent.ainvoke(
            {"messages": "what is the weather in nyc?"}
        )
        print(math_response)
        print(weather_response)


# Ensure the script runs the async main function
if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
