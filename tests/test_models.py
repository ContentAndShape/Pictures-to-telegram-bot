import pytest
from bot.models import User


class TestUser:
    def test_correct_user_init(self):
        user = User("1", "Alex")
        assert user.id == "1"
        assert user.username == "Alex"
        assert user.hashtags == []
        assert user.filter == None

    def test_set_hashtags(self):
        user = User("1", "Alex")
        # Change user's hashtags:
        user.hashtags = ["foo", "bar"]
        user.set_hashtags("sphynx", "food", "sport")
        assert user.hashtags == ["sphynx", "food", "sport"]
        # Clear user's hashtags:
        user.set_hashtags()
        assert user.hashtags == []

    def test_add_hashtags(self):
        user = User("1", "Alex")
        # user.hashtags = [] by default
        user.add_hashtags("sphynx", "food", "sport")
        assert user.hashtags == ["sphynx", "food", "sport"]
        # Add hashtags:
        user.add_hashtags("foo", "bar")
        assert user.hashtags == ["sphynx", "food", "sport", "foo", "bar"]

    def test_remove_hashtags(self):
        user = User("1", "Alex")
        user.set_hashtags("sphynx", "food", "sport")
        # Try to remove existing hashtags:
        user.remove_hashtags("food", "sport")
        assert user.hashtags == ["sphynx"]
        # Try to remove non-existing hashtag:
        with pytest.raises(ValueError):
            user.remove_hashtags("bar")
