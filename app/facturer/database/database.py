from flask_pymongo import PyMongo


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self) -> None:
        pass  # not needed


database = Database()


def initialize_db(app):
    app.config["MONGO_URI"] = "mongodb://localhost:27017/facturer"
    mongodb_client = PyMongo(app)
    database.db = mongodb_client.db
