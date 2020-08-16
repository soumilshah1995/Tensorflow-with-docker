try:
    from flask import Flask, request
    from flask_restful import Resource, Api, reqparse
    from API.Controller.views import Embeddings
    print("ALL OK ")
except Exception as e:
    print("Some Modules are Missing {}".format(e))


app = Flask(__name__)
api = Api(app)
