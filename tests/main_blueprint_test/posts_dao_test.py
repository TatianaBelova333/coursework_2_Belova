import pytest


class TestPostDAO:
    def test_load_date(self, posts_dao):
        data = posts_dao.load_data('text.txt')
        assert data == [], 'Ошибка обработки ошибок FileNotFoundError, JSONDecodeError'

    def test_get_all_posts(self, posts_dao, keys_expected):
        posts = posts_dao.get_all_posts()
        assert type(posts) == list, 'Возвращаемые данные - не список'
        assert len(posts) > 0, 'Возвращается пустой список'
        assert set(posts[0].keys()) == keys_expected, 'неверный список ключей'

    def test_get_posts_with_links_added(self, posts_dao, keys_expected):
        posts = posts_dao.get_posts_with_links_added()
        assert type(posts) == list, 'Возвращаемые данные - не список'
        assert len(posts) > 0, 'Возвращается пустой список'
        assert set(posts[0].keys()) == keys_expected, 'неверный список ключей'

    def test_get_post_by_pk(self, posts_dao, keys_expected):
        post = posts_dao.get_post_by_pk(1)
        assert post['pk'] == 1, 'возвращается неверный пост'
        assert type(post) == dict, 'возвращается не словарь'
        assert set(post.keys()) == keys_expected, 'неверный список ключей'

    def test_get_posts_by_user(self, posts_dao):
        posts = posts_dao.get_posts_by_user('leo')
        assert len(posts) == 2, 'Неверное количество постов для пользователя leo'
        assert posts[0]['poster_name'] == 'leo', 'неверный автор'
        assert type(posts) == list, 'возвращается не список'

    def test_get_post_comments(self, posts_dao, comment_keys_expected):
        comments = posts_dao.get_post_comments(1)
        assert type(comments) == list, 'возвращается не список'
        assert len(comments) > 0, 'возвращается пустой список'
        assert set(comments[0].keys()) == comment_keys_expected, 'неверный список ключей'
        assert comments[0]['pk'] == 1, 'возвращается неверный комментарий'

    def test_get_posts_by_user_query(self, posts_dao):
        posts = posts_dao.get_posts_by_user_query('fhfhf')
        assert type(posts) == list, 'возвращается не список'
        assert len(posts) == 0, 'cписок непустой'
