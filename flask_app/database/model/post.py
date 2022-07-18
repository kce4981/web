from flask_app.database import db
from flask_app.database.model.post_user_likes import User_Post_likes
from flask_app.database.utils.utils import format_model

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    likes = db.relationship('User', secondary=User_Post_likes, backref='likes')

    def format(self) -> dict:
        return format_model(self, ['id', 'title', 'content', 'author_id', 'likes'])