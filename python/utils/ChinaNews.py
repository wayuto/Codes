# %%
from requests import *
from bs4 import BeautifulSoup
from typing import Callable
import time
import os

import asyncio
import aiohttp
import aiofiles

# %%
import nest_asyncio

nest_asyncio.apply()

# %%
START_PAGE = 1
MAX_CONCURRENT = 10
TIMEOUT = 3

domain: str = "www.chinanews.com"
headers: dict = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# %%
async def parse_and_save(text, page, domain) -> bool:
    soup: BeautifulSoup = BeautifulSoup(text, "html.parser")

    u_titles = soup.find_all("div", "dd_bt")
    u_tags = soup.find_all("div", "dd_lm")
    u_times = soup.find_all("div", "dd_time")
    u_urls = soup.find_all("div", "dd_bt")

    urls = [f"https://{domain}{url.select("a")[0].get("href")}" for url in u_urls]
    titles = [title.get_text() for title in u_titles]
    tags = [tag.get_text() for tag in u_tags]
    times = [time.get_text() for time in u_times]

    try:
        os.makedirs("ChinaNews", exist_ok=True)
        async with aiofiles.open(f"ChinaNews/Page{page}.md", "w") as f:
            for i in range(len(titles)):
                await f.write(f"""
***<font size="7">标题: [{titles[i]}]({urls[i]})</font>***  

**<font size="5">标签: {tags[i]}</font>**  

*<font size="3">时间: {times[i]}</font>*  

---
                """)
        print(f"Page {page} has been Saved.")
        return True

    except Exception as e:
        print(f"Page {page}: Parsing error - {str(e)}")
        return False

# %%
async def scrape_page(session, page, domain, headers) -> bool:
    request_url: str = f"https://{domain}/scroll-news/news{page}.html"
    try:
        async with session.get(request_url, headers=headers) as res:
            if res.status != 200:
                print(f"Page {page}: Status {res.status} - Stopping")
                return False

            print(f"Page {page}: Scraping (Status {res.status})")
            content = await res.text()
            return await parse_and_save(content, page, domain)

    except Exception as e:
        # print(f"Page {page}: Error - {str(e)}")
        return False

# %%
async def main(domain, headers="", start_page=1, max_concurrent=10, time_out=10):
    connector = aiohttp.TCPConnector(limit=max_concurrent)
    timeout = aiohttp.ClientTimeout(total=time_out)

    async with aiohttp.ClientSession(
            connector=connector,
            timeout=timeout,
            headers=headers
    ) as session:
        tasks = []
        page = start_page
        active_tasks = 0
        last_valid_page = start_page - 1
        should_continue = True

        while should_continue:
            while active_tasks < max_concurrent and should_continue:
                task = asyncio.create_task(scrape_page(session, page, domain, headers))
                tasks.append(task)
                page += 1
                active_tasks += 1

            if not tasks:
                break

            done, pending = await asyncio.wait(
                tasks,
                return_when=asyncio.FIRST_COMPLETED
            )

            for task in done:
                try:
                    success = await task
                    active_tasks -= 1

                    if success:
                        last_valid_page = max(last_valid_page, page - active_tasks - 1)
                    else:
                        should_continue = False
                        print(f"All pages have been scraped.")
                        break

                except Exception as e:
                    print(f"Task error: {str(e)}")
                    active_tasks -= 1
                    should_continue = False
                    break

            tasks = list(pending)

            if not tasks and not should_continue:
                break

        print(f"Last valid page: {last_valid_page}")

# %%
print("Starting asynchronous scraping...")
start_time: float = time.time()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(
    domain=domain,
    headers=headers,
    start_page=START_PAGE,
    max_concurrent=MAX_CONCURRENT,
    time_out=TIMEOUT
))

duration: float = time.time() - start_time
print(f"Scraping completed in {duration:.2f} secs.")

# %%