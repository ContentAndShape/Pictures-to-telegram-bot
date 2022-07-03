from dataclasses import dataclass, field


@dataclass
class User:
    """
    id: user's id,
    username: user's username,
    hashtags: search hashtag chosen by user,
    filter: filter mode chosen by user.\n
    User class contains required user info and its configurations.
    This class is requried to create user instances and save them into database.
    """

    id: str
    username: str
    hashtags: list[str] = field(default_factory=list)
    filter: str = None

    def set_hashtags(self, *hashtags: str) -> None:
        """Replaces old hashtag list with the list of provided hashtags"""
        self.hashtags = [hashtag for hashtag in hashtags]

    def add_hashtags(self, *hashtags: str) -> None:
        """Appends the provided hashtags to existing hashtag list"""
        for hashtag in hashtags:
            self.hashtags.append(hashtag)

    def remove_hashtags(self, *hashtags: str) -> None:
        """Remove certain provided hashtags"""
        for hashtag in hashtags:
            if hashtag in self.hashtags:
                self.hashtags.remove(hashtag)
            else:
                raise ValueError(f"{hashtag} not in {self.username}'s hashtags")
