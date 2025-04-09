import aiohttp
import time
import asyncio

class AsyncWebScrapper:
    def __init__(self, urls):
        self.urls = urls

    async def fetch(self, session, url, retries=3) -> str:
        for attempt in range(retries):
            try:
                async with session.get(url) as response:
                    response.raise_for_status()
                    return await response.text()
            except aiohttp.ClientError as e:
                print(f"Client error fetching {url}: {e}")
            except asyncio.TimeoutError:
                print(f"Timeout fetching {url}")
            except Exception as e:
                print(f"Unexpected error fetching {url}: {e}")
            
            # Wait before retrying
            await asyncio.sleep(2 ** attempt)
        return ""

    async def fetch_all(self) -> list:
        semaphore = asyncio.Semaphore(5)  # Limit to 5 concurrent requests
        timeout = aiohttp.ClientTimeout(total=30)

        async with aiohttp.ClientSession(timeout=timeout) as session:
            async def limited_fetch(url):
                async with semaphore:
                    return await self.fetch(session, url)

            tasks = [limited_fetch(url) for url in self.urls]
            return await asyncio.gather(*tasks)

if __name__ == "__main__":
    urls = [
        "https://en.wikipedia.org/wiki/Python_(programming_language)", 
        "https://en.wikipedia.org/wiki/Vimy_Ridge_Day",
        "https://en.wikipedia.org/wiki/Food_safety",
        "https://en.wikipedia.org/wiki/Health"
    ] # Example URLs, replace with actual URLs
    
    scrapper = AsyncWebScrapper(urls)
    start_time = time.time()
    
    try:
        results = asyncio.run(scrapper.fetch_all())
    except RuntimeError:
        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(scrapper.fetch_all())
    
    end_time = time.time()

    print(f"Fetched {len(results)} URLs in {end_time - start_time:.2f} seconds")
    
    for result in results:
        print(result[:100])  # Print the first 100 characters of each result