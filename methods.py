import json
from ml import generate_data, normalization, insertknearestneighbor, update_ranking
from flask import Flask, request, Blueprint

methods = Blueprint('methods', __name__)

app = Flask(__name__)

def get_hotel_response(picks, hotel_data, rankings):
    dictio = json.dumps({"id":5,"accrej":0})
    dictio = json.loads(dictio)
#    feedback = request.get_json()
    if dictio["accrej"] == 1: picks[dictio["id"]] = True
    if dictio["accrej"] == 0:
        print(picks[dictio["id"]])
        print(rankings[dictio["id"]])
        picks[dictio["id"]] = False
        rankings[dictio["id"]] = 0
        print(picks[dictio["id"]])
        print(rankings[dictio["id"]])



picked, hotels, ranking = generate_data()
normal_hotels = normalization(hotels)
model = insertknearestneighbor(hotels)
get_hotel_response(picked, hotels, ranking)
