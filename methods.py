import json
from ml import generate_data, normalization, insertknearestneighbor, update_ranking
from flask import Flask, request, Blueprint

methods = Blueprint('methods', __name__)

app = Flask(__name__)

def get_hotel_response(picks, hotel_data, rankings, models, hotelnorm):
    dictio = json.dumps({"id":5,"accrej":0})
    dictio = json.loads(dictio)
#    feedback = request.get_json()
    if dictio["accrej"] == 1: picks[dictio["id"]] = True
    if dictio["accrej"] == 0:
        picks[dictio["id"]] = False
        rankings[dictio["id"]] = 0
    print(hotelnorm[dictio["id"]])
    print(update_ranking(dictio["id"], dictio["accrej"], models, hotelnorm[dictio["id"]], rankings))



picked, hotels, ranking = generate_data()
normal_hotels = normalization(hotels)
print(normal_hotels[0])
model = insertknearestneighbor(normal_hotels)
get_hotel_response(picked, hotels, ranking, model, normal_hotels)
