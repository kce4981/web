from flask import Flask


def create_app() -> Flask:
    from flask_app.routes import blueprints
    from flask_app.database import init_db

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/app.db'

    with app.app_context():
        init_db()

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app
