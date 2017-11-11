import numpy as np
import random
from sklearn import neighbors as knn
from sklearn.neighbors import DistanceMetric as dm
from flask import Flask, request, redirect, url_for, render_template, Blueprint


ml = Blueprint('ml', __name__)

app = Flask(__name__)

def generate_data():
    data = []
    picked = []
    ranking = [1 for i in range(0, 1000)]
    topick = [None, True, False]
    for i in range(0, 1000):
        picked.append(random.choice(topick))
        features = [random.randrange(1, 1001), random.randrange(0, 101), random.randrange(0, 2), random.randrange(0, 101)/100, random.randrange(1, 11), random.randrange(0, 2)]
        data.append(features)
    return picked, data, ranking

def normalization(hotel_data):
    minmaxs = []
    normhotels = []
    for i in range(0, len(hotel_data[0])):
        min = hotel_data[0][i]
        max = hotel_data[0][i]
        for hotel in range(0, len(hotel_data)):
            if hotel_data[hotel][i] > max:
                max = hotel_data[hotel][i]
            if hotel_data[hotel][i] < min:
                min = hotel_data[hotel][i]
        minmaxs.append((min, max-min))
    for i in range(0, len(hotel_data)):
        hotelnormfeatures = []
        for k in range(0, len(hotel_data[i])):
            hotelnormfeatures.append((hotel_data[i][k] - minmaxs[k][0])/(minmaxs[k][1]))
        normhotels.append(hotelnormfeatures)
    return normhotels

def insertknearestneighbor(data):
    model = knn.NearestNeighbors(1)#, n_jobs=2)
    model.fit(data)
    return model

def update_ranking(id, acc_or_rej, model, hotel_data, rankings):
    results = model.kneighbors(np.asarray(hotel_data[id]).reshape(1, -1), n_neighbors=5, return_distance=True)
    distances = results[0].tolist()[0]
    indices = results[1].tolist()[0]
    for i in range(0, len(indices)):
        if acc_or_rej:
            try:
                if distances[i] > 1:
                    rankings[indices[i]]+= 0.9/distances[i]
                else:
                    rankings[indices[i]] += 0.9 * distances[i]
            except (ZeroDivisionError):
                rankings[indices[i]] += 1
        else:
            try:
                if distances[i] > 1:
                    rankings[indices[i]] -= 0.9/distances[i]
                else:
                    rankings[indices[i]] -= 0.9 * distances[i]
            except (ZeroDivisionError):
                rankings[indices[i]] = 0
    return rankings

