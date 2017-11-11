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

def normalization():
    minmaxs = []
    normhotels = []
    for i in range(0, len(hotels[0])):
        min = hotels[0][i]
        max = hotels[0][i]
        for hotel in range(0, len(hotels)):
            if hotels[hotel][i] > max:
                max = hotels[hotel][i]
            if hotels[hotel][i] < min:
                min = hotels[hotel][i]
        minmaxs.append((min, max-min))
    for i in range(0, len(hotels)):
        hotelnormfeatures = []
        for k in range(0, len(hotels[i])):
            hotelnormfeatures.append((hotels[i][k] - minmaxs[k][0])/(minmaxs[k][1]))
        normhotels.append(hotelnormfeatures)
    return normhotels

def insertknearestneighbor(data):
    model = knn.NearestNeighbors(1, n_jobs=2)
    model.fit(data)
    return model

def update_ranking(id, acc_or_rej, model):
    results = model.kneighbors(np.asarray(hotels[id]).reshape(1, -1), n_neighbors=5, return_distance=True)
    print(results[0].tolist())
    for i in range(0, len(results[1])):
        print(results[1][0][i])


picked, hotels, ranking = generate_data()
normal_hotels = normalization()
model = insertknearestneighbor(hotels)
update_ranking(5, True, model)