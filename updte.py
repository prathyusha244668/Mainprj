from flask import Flask, jsonify, request
import json
from flask_pymongo import PyMongo

from flask import request

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/academic_report"
mongo = PyMongo(app)



@app.route('/newsub', methods=['put'])
def add_sub():
    data = request.get_json()
    subject = data["subject"]
    name = data["name"]
    n_id = mongo.db.faculty.update({'subject': 'usha', 'name': 'flask'},{"$set":{'subject': subject, 'name': name}})
    new_en = mongo.db.faculty.find_one({'_id': n_id })
    #output = {'subject' : new_en['subject'], 'name' : new_en['name']}
    return jsonify({'result' : n_id})

if __name__=='__main__':
    app.run()
