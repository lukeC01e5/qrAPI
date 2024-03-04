
import os

from flask import Flask, Response, request, jsonify, make_response
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://colesluke:WZAQsanRtoyhuH6C@qrcluster.zxgcrnk.mongodb.net/playerData"
mongo = PyMongo(app)


@app.route('/api/v1/resources', methods=['GET'])
def get_resources():
    resources = mongo.db.Data.find()
    resp = dumps(resources)
    return resp

if __name__ == "__main__":
    app.run(debug=True)