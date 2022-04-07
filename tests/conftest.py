import pytest
import run
from config.development import POSTS_PATH, COMMENTS_PATH, BOOKMARKS_PATH
from app.main.dao.posts_dao import PostDAO
from app.bookmarks.dao.bookmarks_dao import BookmarkDAO


@pytest.fixture()
def test_client():
    app = run.app
    return app.test_client()


@pytest.fixture()
def keys_expected():
    keys_expected = {
        'poster_name',
        'poster_avatar',
        'pic',
        "content",
        "views_count",
        "likes_count",
        "pk"
    }
    return keys_expected


@pytest.fixture()
def comment_keys_expected():
    comment_keys_expected = {
        "post_id",
        "commenter_name",
        "comment",
        "pk"
    }
    return comment_keys_expected


@pytest.fixture()
def test_client():
    app = run.app
    return app.test_client()


@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostDAO(POSTS_PATH, COMMENTS_PATH)
    return posts_dao_instance


@pytest.fixture()
def bookmarks_dao():
    bookmarks_dao_instance = BookmarkDAO(BOOKMARKS_PATH)
    return bookmarks_dao_instance