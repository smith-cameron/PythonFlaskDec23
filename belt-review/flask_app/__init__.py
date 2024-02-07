from flask import Flask
from flask_cors import CORS
# instance of Flask class imported from flask package
app = Flask(__name__)


CORS(app)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5000"}})