import pytest


class TestBookmarkDAO:
    def test_get_all_bookmarks(self, bookmarks_dao, keys_expected):
        bookmarks = bookmarks_dao.get_all_bookmarks()
        assert type(bookmarks) == list, 'Возвращаемые данные - не список'
        if len(bookmarks) > 0:
            assert set(bookmarks[0].keys()) == keys_expected, 'неверный список ключей'
        else:
            assert bookmarks == [], 'При отсутствии закладок возвращается не пустой список'

    def test_is_in_saved_bookmarks(self, bookmarks_dao):
        bookmarks = bookmarks_dao.is_in_saved_bookmarks('fjkfj')
        assert bookmarks is False, 'Ошибка при возврате данных с несуществующим post_id'

    def test_get_number_of_bookmarks(self, bookmarks_dao):
        number_of_bookmarks = bookmarks_dao.get_number_of_bookmarks()
        assert type(number_of_bookmarks) is int, 'Тип возвращаемых данных - не целое число'
