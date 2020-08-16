try:
    from flask import app,Flask, request
    from flask_restful import Resource, Api, reqparse
    import datetime
    import json
    import os
    import sys
    import tensorflow as tf
    import tensorflow_hub as hub
    import numpy as np
    import ssl
except Exception as e:
    print("Error : {} ".format(e))


global NAME
NAME = os.getenv("NAME")

sys.path.append("Controller")
sys.path.append("API")

app = Flask(__name__)
api = Api(app)


class Tokens(object):

    def __init__(self, word):
        self.word = word

    def token(self):
        module_url = os.getcwd()
        path = os.path.join(module_url, "API/Controller")
        embed = hub.KerasLayer(path)
        embeddings = embed([self.word])
        x = np.asarray(embeddings)
        x = x[0].tolist()
        return x


class Embeddings(Resource):

    def __init__(self):
        self.name = parser.parse_args().get('name', None)

    def get(self):
        helper = Tokens(word=self.name)
        embedding  = helper.token()

        return {
            "embedding":embedding
        }

parser = reqparse.RequestParser()
parser.add_argument("name", type=str, required=True, help="This is Required Parameters ")