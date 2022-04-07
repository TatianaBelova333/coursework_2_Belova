import pytest


class TestBookmarks:
    def test_show_all_bookmarks(self, test_client):
        response = test_client.get('/bookmarks', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код главной ленты - неверный'

    def test_add_bookmark(self, test_client):
        response = test_client.get('/search?query=j%3Blkj', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код страницы результата поиска - неверный'

    def test_remove_bookmarks(self, test_client):
        response = test_client.get('/posts/1', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код первого поста - неверный'

