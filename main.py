from flask import Flask
from src.controller.index import index_api
import os

# DATASET = os.path.join('src/static', 'dataset')


app = Flask(__name__)

app.register_blueprint(index_api,static_folder=None)
# app.config['UPLOAD_FOLDER'] = DATASET


if __name__ == "__main__":
    app.run()