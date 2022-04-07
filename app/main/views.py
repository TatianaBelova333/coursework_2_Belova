from flask import request, render_template, Blueprint
from app.bookmarks.views import bookmarks
from app.main.dao.posts_dao import PostDAO
from config.development import POSTS_PATH, COMMENTS_PATH


posts = PostDAO(POSTS_PATH, COMMENTS_PATH)

main_page_blueprint = Blueprint('main_page', __name__, template_folder='templates')


@main_page_blueprint.route('/')
def page_index():
    all_posts = posts.get_posts_with_links_added()
    number_of_bookmarks = bookmarks.get_number_of_bookmarks()
    return render_template('index.html', posts=all_posts, number_of_bookmarks=number_of_bookmarks)


@main_page_blueprint.route('/search', methods=['GET'])
def search_for_post():
    query = request.args.get('query')
    if not query or set(query) == {' '}:  # if search bar left blank or contains whitespaces only
        return page_index()
    posts_found = posts.get_limited_num_of_posts_found(query, 10)
    number_of_found_posts = len(posts_found)
    return render_template('search.html',
                           number_of_found_posts=number_of_found_posts,
                           posts=posts_found)


@main_page_blueprint.route('/posts/<int:post_id>')
def show_post_by_id(post_id):
    post = posts.get_post_by_pk(post_id)
    comments = posts.get_post_comments(post_id)
    number_of_comments = len(comments)
    return render_template("post.html",
                           post=post,
                           number_of_comments=number_of_comments,
                           comments=comments)


@main_page_blueprint.route('/users/<user_name>')
def show_user_feed(user_name):
    user_feed = posts.get_posts_by_user(user_name)
    return render_template("user-feed.html",
                           user_feed=user_feed,
                           user_name=user_name)


