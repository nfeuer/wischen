import os
import json
from ml import ml, generate_data, normalization, insertknearestneighbor
from methods import methods, get_hotel_response
from flask_restful import Resource, Api, reqparse
from flask import Flask, render_template

app = Flask(__name__)
api = Api(app)
app.register_blueprint(ml, url_prefix='/ml')
app.register_blueprint(methods, url_prefix='/methods')


class HotelList(Resource):
    def __init__(self):
        self.picked, self.hotels, self.ranking = generate_data()
        self.normal_hotels = normalization(self.hotels)
        self.model = insertknearestneighbor(self.normal_hotels)

    def get(self):
        return self.hotels

    def post(self):
        with app.app_context():
            parser = reqparse.RequestParser()
            parser.parse_args()
            dictio = json.dumps({"id": 1, "accrej": 1})
            dictio = json.loads(dictio)
            self.picked, self.hotels, self.ranking, self.normal_hotels = get_hotel_response(dictio, self.picked,
                                                                                                    self.hotels,
                                                                                                    self.ranking,
                                                                                                    self.model,
                                                                                                    self.normal_hotels)
        return self.hotels[0:100]


api.add_resource(HotelList, '/')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
