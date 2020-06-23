from flask import Flask
from src.controller.index import index_api
import os



app = Flask(__name__)
app.register_blueprint(index_api,static_folder=None)


if __name__ == "__main__":
    app.run()