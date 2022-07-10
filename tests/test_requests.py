import aiohttp
import pytest
from bot.main import get_url_list, website_search


PLATFORM = "yandex"
HASHTAG = "Sphynx"
LIMIT = 20


class TestWebSearch:
    @pytest.mark.asyncio
    async def test_website_search(self):
        async with aiohttp.ClientSession() as session:

            html_doc = await website_search(
                session=session, 
                platform=PLATFORM, 
                hashtag=HASHTAG)
            assert type(html_doc) == str


class TestMain:
    @pytest.mark.asyncio
    async def test_get_url_list(self):
        urls = await get_url_list(platform=PLATFORM, hashtag=HASHTAG, limit=LIMIT)
        assert len(urls) == LIMIT
        for url in urls:
            assert url.startswith("//")
