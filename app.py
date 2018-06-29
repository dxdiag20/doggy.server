import os
from flask import Flask, request, send_from_directory, json, jsonify

import breeds
from doggyML.dog_classify import classify_image

def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def getDogBreeds():
        return json.jsonify(breeds.dogBreeds)

    @app.route("/", methods=['POST'])
    def index():
        if not 'image' in request.files:
            content = {'error': 'please send an image'}
            return content, 400
       
        file = request.files['image']
        file.save(file.filename)

        return classify_image(file.filename)

    @app.route('/static/<path:path>', methods=['GET'])
    def send_static(path):
        return send_from_directory('static', path)
    
    return app
