import flask


class app():
    flask = flask.Flask('app')

    def __init__(self) -> None:
        pass
        
    def getFlask(self) -> flask.Flask:
        return app.flask