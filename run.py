import os
from ml import ml, generate_data, normalization, insertknearestneighbor
from methods import methods
from flask_restful import Resource, Api
from flask import Flask, render_template


app = Flask(__name__)
api = Api(app)
app.register_blueprint(ml, url_prefix='/ml')
app.register_blueprint(methods, url_prefix='/methods')

class HelloWorld(Resource):
    def __init__(self):
        self.picked, self.hotels, self.ranking = generate_data()
        self.normal_hotels = normalization(self.hotels)
        self.model = insertknearestneighbor(self.normal_hotels)
    def get(self):
        return self.normal_hotels
    def post(self):
        pass
api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)