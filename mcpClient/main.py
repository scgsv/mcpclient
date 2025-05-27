from fastmcp import Client
import asyncio
from fastmcp.client.transports import StreamableHttpTransport


transport = StreamableHttpTransport(url="http://127.0.0.1:7777/mcp")
client = Client(transport)



async def main():
    async with client:
        tools = await client.list_tools()
        print(f"Available tools: {tools}")


async def list_tables():
    async with client:
        tools = await client.call_tool("list_tables")
        print(f"Available tools: {tools}")




asyncio.run(main())

asyncio.run(list_tables())