
from app.facturer.database.database import initialize_db
from flask import Flask


def create_app():
    app = Flask(__name__)
    initialize_db(app)
    # we do this as we have to wait the bd to be loaded before load this controllers
    from app.facturer.controller import mod as facturer_module
    app.register_blueprint(facturer_module)
    return app
