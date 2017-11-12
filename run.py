from flask import Flask, request
#from flask_restful import Resource, Api
import os
from flask import jsonify
import json
from ml import ml, generate_data, normalization, insertknearestneighbor
from methods import methods, get_hotel_response

app = Flask(__name__)  # create the application instance :)
app.config.from_object(__name__)  # load config from this file , flaskr.py

picked, hotels, ranking = generate_data()
normal_hotels = normalization(hotels)
model = insertknearestneighbor(normal_hotels)

@app.route(r'/')
def allhotels():
    global picked
    global hotels
    global ranking
    global model
    global normal_hotels
    picked, hotels, ranking = generate_data()
    normal_hotels = normalization(hotels)
    model = insertknearestneighbor(normal_hotels)
    return jsonify(hotels[0:50])
@app.route(r'/posting', methods=['GET'])
def specifichotels():
    global picked
    global hotels
    global ranking
    global model
    global normal_hotels
    with app.app_context():
        fromserver = {"id": int(request.args.get("id")), "accrej": int(request.args.get("accrej"))  }
        print(fromserver)
        picked, hotels, ranking, normal_hotels = get_hotel_response(fromserver, picked, hotels, ranking, model, normal_hotels)
    return jsonify(hotels[0:2])


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



#
# from flask_restful import Resource, Api, reqparse
# from flask import Flask, render_template, request
#
# app = Flask(__name__)
# api = Api(app)
# app.register_blueprint(ml, url_prefix='/ml')
# app.register_blueprint(methods, url_prefix='/methods')
#
# picked, hotels, ranking = generate_data()
# normal_hotels = normalization(hotels)
# model = insertknearestneighbor(normal_hotels)
#
# class HotelList(Resource):
#     def get(self):
#         return hotels
#     def post(self):
#         global picked
#         global hotels
#         global ranking
#         global model
#         global normal_hotels
#         with app.app_context():
#             request_json = request.get_json()
#             value1 = request_json.get('id')
#             print(value1)
#             id = request.json["id"]
#             print(id)
#             picked, hotels, ranking, normal_hotels = get_hotel_response(id, picked, hotels, ranking, model, normal_hotels)
#         return hotels[0:2]
#
#
# api.add_resource(HotelList, '/')
#
# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
# #    app.run(host='0.0.0.0', port=port)
#     app.run()
#
