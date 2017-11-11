from flask import Flask, request, Blueprint

from ml import update_ranking

api = Blueprint('api', __name__)

app = Flask(__name__)

@app.route('/', methods=["POST"])
def get_hotel_response():
    feedback = request.get_json()
    update_ranking()
    return feedback