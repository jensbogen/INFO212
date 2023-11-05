from flask import Flask
from my_dao import *

app = Flask(__name__)


@app.route('/save_car', methods=['POST'])
def save_car_info():
    record = json.loads(request.data)
    print(record)