from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/climate', methods=['GET'])
def get_room_climate():
    return 'This is a placeholder for room climate'


@app.route('/climate', methods=['POST'])
def insert_new_climate():
    return 'This is a placeholder to insert new climate'

@app.route('/')
def health():
    return "OK"
