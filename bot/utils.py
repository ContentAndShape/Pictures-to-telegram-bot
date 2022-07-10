"""Module containing utility functions"""

import bs4


def parse_photo_url(html: str, limit: int = 20) -> list[str]:
    """Rerurns a list of urls inside <img> tag"""
    soup = bs4.BeautifulSoup(html, "html.parser",)
    tag_list = soup.find_all("img", limit=limit+1)
    urls = [tag["src"] for tag in tag_list]
    return urls
