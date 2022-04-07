from flask import render_template, Blueprint
from app.main.views import posts


hashtags_blueprint = Blueprint('hashtags', __name__, template_folder='templates')


@hashtags_blueprint.route('/<tag>')
def show_posts_by_tag(tag):
    posts_with_tags = posts.get_posts_by_hashtag(tag)
    return render_template('tag.html', posts=posts_with_tags, tag=tag)


