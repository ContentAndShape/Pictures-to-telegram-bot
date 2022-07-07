"""
This module handles the logic of retrieving data from external sources
"""
import os
import sys
import asyncio
import aiohttp
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import utils
from bot.models import User
from settings import WEBSITE_QUERY_DICT


async def website_search(session, platform: str, hashtag: str) -> requests.Response:
    """Makes a request to provided platform with provided hashtag"""
    async with session.get(f"{WEBSITE_QUERY_DICT[platform]}{hashtag}") as response:
        print(f"Status: {response.status}")
        html_doc = await response.text()
        return html_doc


async def main(platform: str, hashtag: str, limit: int = 20):
    async with aiohttp.ClientSession() as session:
        html = await website_search(session=session, platform=platform, hashtag=hashtag)
        urls = utils.parse_photo_url(html=html, limit=limit)

        for url in urls:
            print(url)
    

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(platform="yandex", hashtag="sphynx", limit=20))
