from flask import jsonify, Blueprint
from app.main.views import posts

api_posts_blueprint = Blueprint('api_posts', __name__)


@api_posts_blueprint.route('/')
def page_posts_json():
    data = posts.get_all_posts()
    return jsonify(data)


@api_posts_blueprint.route('/<int:post_id>')
def page_post_by_pk_json(post_id):
    post = posts.get_post_by_pk(post_id)
    return jsonify(post)





