from flask import Flask, jsonify,request
import json
from flask_pymongo import PyMongo

from bson.json_util import dumps


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/pst"
mongo = PyMongo(app)



@app.route('/datapost', methods=["post"])
def pst_data():
    name = request.json["name"]
    n = mongo.db.usha.find_one({"name":name})
    n.pop("_id")
    #new_en = mongo.db.pst.find()
    #output = {'subject' : new_en['subject'], 'name' : new_en['name']}

    return jsonify({'result' : n})

    

if __name__ == '__main__':
    app.run(debug=True)

