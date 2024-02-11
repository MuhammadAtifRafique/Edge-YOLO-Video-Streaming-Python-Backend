from flask import Flask, jsonify, render_template,request
from flask_socketio import SocketIO,emit,send
from flask_cors import CORS, cross_origin
import base64
import cv2
import time
from dataBase import DataBase
from save_ import Save_
from config import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app)
app.app_context().push()


if __name__ == "__main__":
    obj = Save_()
    obj.start()