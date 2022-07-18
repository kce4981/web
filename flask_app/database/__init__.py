from flask_sqlalchemy import SQLAlchemy
from flask import current_app


def import_models():
    import flask_app.database.model

def init_db():
    global db
    db = SQLAlchemy(current_app)
    import_models()
    db.create_all()

def addObj(obj: object):
    db.session.add(obj)
    db.session.commit()
