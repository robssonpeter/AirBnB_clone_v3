#!/usr/bin/python3
""" The new flask based api """
from flask import Flask
from models.engine.file_storage import FileStorage

from api.v1.views import app_views
from os import environ

storage = FileStorage()
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down():
    storage.close()


if __name__ == "__main__":
    host = environ.get("HBNB_API_HOST", "0.0.0.0")
    port = environ.get("HBNB_API_PORT", 5000)
    app.run(host=host, port=port, threaded=True)
