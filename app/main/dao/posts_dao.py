import json


class PostDAO:
    def __init__(self, posts_path, comments_path):
        self.posts_path = posts_path
        self.comments_path = comments_path

    def load_data(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            return data
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def get_all_posts(self):
        posts = self.load_data(self.posts_path)
        return posts

    def get_posts_with_links_added(self):
        """
        Finds posts with #, converts into hashtags with links and returns all posts (with or without hashtags)
        :return: list
        """
        all_posts = self.get_all_posts()
        posts_with_hashtags = []
        for post in all_posts:
            content = post.get('content').split()
            for i in range(len(content)):
                if content[i].startswith('#'):
                    content[i] = "<a href='/tag/" + content[i][1:] + "'>" + content[i] + "</a>"
                    post['content'] = ' '.join(content)
            posts_with_hashtags.append(post)
        return posts_with_hashtags

    def get_post_by_pk(self, post_pk):
        posts = self.get_posts_with_links_added()
        for post in posts:
            if post_pk == post.get('pk'):
                return post
        return []

    def get_posts_by_user(self, user_name):
        posts = self.get_posts_with_links_added()
        posts_by_user = [post for post in posts if post.get('poster_name') == user_name]
        # sort by pk
        posts_by_user = sorted(posts_by_user, key=lambda x: x['pk'])
        return posts_by_user

    def get_post_comments(self, post_id):
        comments = self.load_data(self.comments_path)
        comments_by_post_id = [comment for comment in comments if comment.get('post_id') == post_id]
        # sort by pk
        comments_by_post_id = sorted(comments_by_post_id, key=lambda x: x['pk'])
        return comments_by_post_id

    def get_posts_by_user_query(self, user_query):
        query = user_query.lower()
        all_posts = self.get_posts_with_links_added()
        posts_found = []
        for post in all_posts:
            if query in post.get('content', '').lower() or query in post.get('poster_name', '').lower():
                posts_found.append(post)
        return posts_found

    def get_posts_by_hashtag(self, hashtag):
        posts_with_hashtag = []
        hashtag = '#' + hashtag
        posts = self.get_posts_with_links_added()
        for post in posts:
            if hashtag in post.get('content'):
                posts_with_hashtag.append(post)
        return posts_with_hashtag





