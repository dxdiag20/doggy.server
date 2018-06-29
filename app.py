import os
from flask import Flask, request, send_from_directory, json, jsonify

import breeds
from doggyML.dog_classify import classify_image

from waitress import serve

import wikipedia
wikipedia.set_lang("ko")

def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def getDogBreeds():
        return json.jsonify(breeds.dogBreeds)

    @app.route("/", methods=['POST'])
    def index():
        if not 'image' in request.files:
            content = {'error': 'please send an image'}
            return json.jsonify(content), 400
       
        file = request.files['image']
        file.save(file.filename)

        breed = classify_image(file.filename)
        page = wikipedia.page(breed)
        description = page.content.split('\n')[0]
        wiki_url = page.url

        return json.jsonify({
            'breed': breed,
            'description': description,
            'wiki_url': wiki_url
        })

    @app.route('/static/<path:path>', methods=['GET'])
    def send_static(path):
        return send_from_directory('static', path)
    
    return app

serve(create_app(), listen='*:8080')
