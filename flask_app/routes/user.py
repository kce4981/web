import flask

user_bp = flask.Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('', methods=['GET'])
def getUser():
    from flask_app.database.model import User

    return {y['name']: y for y in [x.format() for x in User.query.all()]}, 200

@user_bp.route('', methods=['POST'])
def addUser():
    from flask import request
    from flask_app.database import addObj
    from flask_app.database.model import User

    form = request.form

    name = form.get('name', None)
    password = form.get('password', None)
    email = form.get('email', None)
    if not (name and password and email):
        return '', 403 

    newUser = User(name=name, password=password, email=email)
    addObj(newUser)
    
    return '',200

