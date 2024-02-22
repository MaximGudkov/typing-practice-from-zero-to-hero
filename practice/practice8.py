"""
8. Annotating Asynchronous Code

Task: Annotate an asynchronous function fetch_data that retrieves data from an API and returns a parsed JSON response.
Use Awaitable and asyncio.

Task2: Create an async generator stream_results that receives a list of URLs, fetches and processes data from each URL
asynchronously, and yields the results one by one. Annotate this function with AsyncGenerator.
"""

import asyncio
from typing import Awaitable, Dict, AsyncGenerator

StrDict = Dict[str, str]


async def fetch_data(url: str) -> StrDict:
    await asyncio.sleep(1)  # Simulate network delay
    return {"url": url, "data": "Some data from " + url}


def async_fetch_data(url: str) -> Awaitable[StrDict]:  # or Coroutine[Any, Any, StrDict]
    return fetch_data(url)


async def stream_results(urls: list[str]) -> AsyncGenerator[Dict[str, str], None]:
    for url in urls:
        data = await async_fetch_data(url)
        yield data


async def main():
    urls = ["http://example.com/api/data1", "http://example.com/api/data2"]
    async for result in stream_results(urls):
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
