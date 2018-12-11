from flask import Flask, jsonify
from flask_pymongo import PyMongo

from bson.json_util import dumps


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/academic_report"
mongo = PyMongo(app)


@app.route('/')
def test():
    cursor =mongo.db.marks.find({ "$and":[{"subject": "Mathematics"},{"marks":{"$gt":90}}]})

    b={}
    for i in cursor:
        if i["subject"] not in b:
            b[i["name"]]=i["marks"]
    
    return jsonify({"best":max(b.items(),key=lambda x:x[1])})

if __name__=='__main__':
    app.run()

