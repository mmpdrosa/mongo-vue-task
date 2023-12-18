# models.py
from flask_pymongo import PyMongo

mongo = PyMongo()


def init_app(app):
    mongo.init_app(app)
    print(mongo.db)


class Video:
    def __init__(self, name, url, theme, thumbs_up=0, thumbs_down=0):
        self.name = name
        self.url = url
        self.theme = theme
        self.thumbs_up = thumbs_up
        self.thumbs_down = thumbs_down

    def json(self):
        return {
            "name": self.name,
            "url": self.url,
            "theme": self.theme,
            "thumbs_up": self.thumbs_up,
            "thumbs_down": self.thumbs_down,
        }
