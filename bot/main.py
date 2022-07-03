import requests

from settings import HASHTAGS, FILTER
from bot.models import Client


def hashtag_search(hashtag_name): pass
    #hashtag_node = requests.get("graph.facebook.com/ig_hashtag_search?user_id=")
    #hashtag_id = hashtag_node["id"]


def main():
    r = requests.get('http://google.com')
    print(r.status_code)


if __name__ == '__main__':
    main()
