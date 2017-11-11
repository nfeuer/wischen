import json

from flask import Flask, request, Blueprint

methods = Blueprint('methods', __name__)

app = Flask(__name__)

@app.route('/update', methods=["POST"])
def get_hotel_response():
    print(json.load(json.dumps({"id":5,"accrej":True})))
    feedback = request.get_json()
    print(feedback)
    return feedback

#get_hotel_response()