from flask import Flask

from api import api
from ml import ml

app = Flask(__name__)
app.register_blueprint(ml, url_prefix='/ml')
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()