from flask import request, render_template, Blueprint, redirect
from app.bookmarks.dao.bookmarks_dao import BookmarkDAO
from config.development import BOOKMARKS_PATH

bookmarks_blueprint = Blueprint('bookmarks', __name__, template_folder='templates')

bookmarks = BookmarkDAO(BOOKMARKS_PATH)


@bookmarks_blueprint.route('/')
def show_all_bookmarks():
    all_bookmarks = bookmarks.get_all_bookmarks()
    return render_template('bookmarks.html', posts=all_bookmarks)


@bookmarks_blueprint.route('/add/<int:post_id>')
def add_bookmark(post_id):
    bookmarks.add_bookmark(post_id)
    return redirect(request.referrer)


@bookmarks_blueprint.route("/remove/<int:post_id>")
def remove_bookmark(post_id):
    bookmarks.remove_bookmark(post_id)
    return redirect(request.referrer)


