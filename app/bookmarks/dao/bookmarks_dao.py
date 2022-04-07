import json
from config.development import POSTS_PATH
from app.main.dao.posts_dao import PostDAO


class BookmarkDAO(PostDAO):
    def __init__(self, bookmarks_path, posts_path=POSTS_PATH):
        self.bookmarks_path = bookmarks_path
        self.posts_path = posts_path

    def get_all_bookmarks(self):
        bookmarks = PostDAO.load_data(self, self.bookmarks_path)
        return bookmarks

    def save_data_into_json(self, data):
        try:
            with open(self.bookmarks_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def is_in_saved_bookmarks(self, post_id):
        bookmarks = self.get_all_bookmarks()
        for bookmark in bookmarks:
            if bookmark.get('pk') == post_id:
                return bookmark
        return False

    def get_bookmark_info(self, post_id):
        all_posts = PostDAO.get_posts_with_links_added(self)
        for post in all_posts:
            if post.get('pk') == post_id:
                return post

    def add_bookmark(self, post_id):
        if not self.is_in_saved_bookmarks(post_id):
            new_bookmark = self.get_bookmark_info(post_id)
            all_bookmarks = self.get_all_bookmarks()
            all_bookmarks.append(new_bookmark)
            self.save_data_into_json(all_bookmarks)

    def remove_bookmark(self, post_id):
        bookmark_to_delete = self.is_in_saved_bookmarks(post_id)
        if bookmark_to_delete:
            all_bookmarks = self.get_all_bookmarks()
            all_bookmarks.remove(bookmark_to_delete)
            self.save_data_into_json(all_bookmarks)

    def get_number_of_bookmarks(self):
        all_bookmarks = self.get_all_bookmarks()
        return len(all_bookmarks)

