import json
from ml import generate_data, normalization, insertknearestneighbor, update_ranking
from flask import Flask, request, Blueprint

methods = Blueprint('methods', __name__)

app = Flask(__name__)


def get_hotel_response(responses, picks, hotel_data, rankings, models, hotelnorm):
    #    feedback = request.get_json()
    if responses["accrej"] == 1: picks[responses["id"]] = True
    if responses["accrej"] == 0:
        picks[responses["id"]] = False
        rankings[responses["id"]] = 0

    rankings = update_ranking(responses["id"], responses["accrej"], models, hotelnorm, rankings)
    rankings, hotel_data, hotelnorm, picks = (list(t) for t in
                                              zip(*sorted(zip(rankings, hotel_data, hotelnorm, picks), reverse=True)))
    return picks, hotel_data, rankings, hotelnorm