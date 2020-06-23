from flask import Blueprint, request, render_template, url_for, redirect
from flask import Flask
from keras.engine.saving import load_model
import src.libs.vector_search as vector_search
import os
import time

import io
import numpy as np
from keras.preprocessing.image import img_to_array
from PIL import Image
from keras.applications.vgg16 import preprocess_input
import pandas as pd

index_api = Blueprint('index_api',__name__,
                template_folder='../templates'
                )

loaded_model = load_model('pre-model.hdf5')

features_path = 'feat_4096'
file_mapping = 'index_4096'
images_features, file_index = vector_search.load_features(features_path, file_mapping)
image_index = vector_search.index_features(images_features, dims=4096)

@index_api.route('/')
def home():
    images =[]
    return render_template('home.html',images=images)

@index_api.route('/wordsearch',methods=['GET', 'POST'])
def word():
    if request.method == 'POST':
        text = request.form['query_text']
    #     xử lý text ở đây
        return jsonify(text)
    else:
        return render_template('wordSearch.html')

@index_api.route('/imagesearch',methods=['GET', 'POST'])
def image():
    if request.method == 'POST':
        file = request.files['query_img']
        upload_folder = os.path.join(os.getcwd(), 'static/images-upload')
        
        filename = file.filename
        image_path = os.path.join(upload_folder, filename)
        file.save(image_path)

        # img_requested = file.read()
        
        start_time = time.time()
        images_features_search = vector_search.generate_features_from_image_of_request(image_path, loaded_model)
        images = vector_search.search_index_by_value(images_features_search, image_index, file_index, top_n=5)
        run_time = time.time() - start_time

        df = pd.read_csv('label-link.csv')
        df.set_index('label', inplace=True)

        

        images_result = [[x[0], x[1], x[2], ' '.join(x[1].split('/')[1].split('_')), df.loc[[x[1].split('/')[1]]].values[0,0]] for x in images]     
        result = {
            'run_time': run_time,
            'images': images_result,
            'category': ' '.join(images[0][1].split('/')[1].split('_')),
            'original_image': 'images-upload/' + filename
        }
        return render_template('imageSearch.html', result=result)
    else:
        return render_template('imageSearch.html')



