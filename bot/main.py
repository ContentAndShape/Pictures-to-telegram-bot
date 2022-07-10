"""
This module handles the work of bot
"""
import os
import sys
import aiohttp
import aiogram
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bot import utils

from settings import WEBSITE_QUERY_DICT
from tokens import BOT_TOKEN


async def website_search(session: aiohttp.ClientSession, platform: str, hashtag: str) -> requests.Response:
    """Makes a request to provided platform with provided hashtag"""
    
    if platform not in WEBSITE_QUERY_DICT.keys():
        raise KeyError(f'Platform "{platform}" not in platforms settings.')

    async with session.get(f"{WEBSITE_QUERY_DICT[platform]}{hashtag}") as response:
        print(f"Status: {response.status}")
        html_doc = await response.text()
        return html_doc


async def get_url_list(platform: str, hashtag: str, limit: int = 20):
    async with aiohttp.ClientSession() as session:
        html = await website_search(session=session, platform=platform, hashtag=hashtag)
        urls = utils.parse_photo_url(html=html, limit=limit)[1:]

        return urls
    
    
bot = aiogram.Bot(token=BOT_TOKEN)
dispatcher = aiogram.Dispatcher(bot=bot)


# Test sphynx image
@dispatcher.message_handler(commands=["sphynx"])
async def test_sphynx(message: aiogram.types.Message):
    urls = await get_url_list(platform="yandex", hashtag="sphynx", limit=1)
    for url in urls:
        await message.reply(f"{url}")


@dispatcher.message_handler(commands=[""])
async def send_images():
    pass


if __name__ == "__main__":

    aiogram.executor.start_polling(dispatcher=dispatcher, skip_updates=True)
    # loop = asyncio.get_event_loop()
    # urls = loop.run_until_complete(main(platform="yandex", hashtag="sphynx", limit=20))
