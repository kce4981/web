from flask_app.database import db
from flask_app.database.utils import utils
from flask_app.database.model.post_user_likes import User_Post_likes

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)
    posts = db.relationship('Post', backref='author')

    def format(self) -> dict:
        return utils.format_model(self, ['id', 'name', 'password', 'email', 'posts', 'likes'])