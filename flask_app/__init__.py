from flask import Flask


class FlaskApp:
    
    def __init__(self) -> None:
        
        from flask_app.routes import blueprints
        from flask_app.database import init_db

        self.app = Flask(__name__)
        app = self.app

        with app.app_context():
            init_db()
            load_config()

        for blueprint in blueprints:
            app.register_blueprint(blueprint)


    def run(self) -> None:
        app = self.app
        app.run(
            debug=app.config['debug_'],
            host=app.config['host_'],
            port=app.config['port_']
        )

def load_config():
    from flask import current_app
    from pathlib import Path
    import json
    cfg_location = Path(__file__).parent.resolve().parent / 'config.json'
    with open(cfg_location) as fp:
        current_app.config.update(json.load(fp))