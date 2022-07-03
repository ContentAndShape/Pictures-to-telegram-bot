"""
This module handles the logic of retrieving data from external sources
"""
import os
import sys
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from settings import HASHTAGS, FILTER
from bot.models import User


def hashtag_search(hashtag_name):
    pass


# hashtag_node = requests.get("graph.facebook.com/ig_hashtag_search?user_id=")
# hashtag_id = hashtag_node["id"]


def main():
    pass


# r = requests.get('http://google.com')
# print(r.status_code)


if __name__ == "__main__":
    main()
