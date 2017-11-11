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

picked, hotels, ranking = generate_data()
normal_hotels = normalization(hotels)
model = insertknearestneighbor(normal_hotels)

class HotelList(Resource):
    def get(self):
        return hotels
    def post(self):
        with app.app_context():
            global picked, hotels, ranking, model, normal_hotels
            parser = reqparse.RequestParser()
            parser.parse_args()
            dictio = json.dumps({"id": 1, "accrej": 1})
            dictio = json.loads(dictio)
            picked, hotels, ranking, normal_hotels = get_hotel_response(dictio, picked, hotels, ranking, model, normal_hotels)
        hotels_to_send = hotels[0:2]


api.add_resource(HotelList, '/')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
