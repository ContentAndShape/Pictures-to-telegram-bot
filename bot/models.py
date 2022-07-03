from dataclasses import dataclass


@dataclass
class Client:
    id: str
    username: str = None
    hashtags: list = []

    def set_hashtag(self, *args):
        self.hashtags = [arg for arg in args]
