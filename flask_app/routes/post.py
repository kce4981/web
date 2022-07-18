from flask import Blueprint


post_bp = Blueprint('post', __name__, url_prefix='/post')


@post_bp.route('', methods=['GET'])
def get_post():
    from flask_app.database.model.post import Post

    return {y['title']: y for y in [x.format() for x in Post.query.all()]}, 200


@post_bp.route('', methods=['POST'])
def create_post():
    from flask import request    
    from flask_app.database.model.post import Post
    from flask_app.database import addObj
    form = request.form

    title = form.get('title', None)
    content = form.get('content', None)
    author_id = form.get('author_id', None)

    newPost = Post(title=title, content=content, author_id=author_id)
    addObj(newPost)
    return '', 200