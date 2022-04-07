import pytest


class TestApiPosts:
    def test_api_posts(self, keys_expected, test_client):
        response = test_client.get('/api/posts/', follow_redirects=True)
        assert type(response.json) == list, 'Возвращаемый формат данных - не список'
        for el in response.json:
            assert set(el.keys()) == keys_expected, 'неверный список ключей'

    def test_api_posts_id(self, keys_expected, test_client):
        response = test_client.get('/api/posts/1', follow_redirects=True)
        assert type(response.json) == dict, 'Возвращаемый формат данных - не словарь'
        assert set(response.json.keys()) == keys_expected, 'неверный список ключей'

