import pytest


class TestHashtagsBlueprint:
    def test_show_posts_by_tag(self, test_client):
        response = test_client.get('/tag/еда', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код страницы с хэштегом - неверный'
