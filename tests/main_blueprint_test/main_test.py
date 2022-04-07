import pytest


class TestMainBlueprint:
    def test_page_index(self, test_client):
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код главной ленты - неверный'

    def test_search_for_post(self, test_client):
        response = test_client.get('/search?query=j%3Blkj', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код страницы результата поиска - неверный'

    def test_show_post_by_id(self, test_client):
        response = test_client.get('/posts/1', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код первого поста - неверный'

    def test_show_user_feed(self, test_client):
        response = test_client.get('/users/leo', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код ленты пользователя leo - неверный'
