from flask import Flask
from app.main.views import main_page_blueprint
from app.bookmarks.views import bookmarks_blueprint
from app.hashtags.views import hashtags_blueprint
from app.api_posts.views import api_posts_blueprint


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(main_page_blueprint)
app.register_blueprint(bookmarks_blueprint, url_prefix='/bookmarks')
app.register_blueprint(hashtags_blueprint, url_prefix='/tag')
app.register_blueprint(api_posts_blueprint, url_prefix='/api/posts')


if __name__ == '__main__':
    app.run(debug=True)

