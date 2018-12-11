from flask import Flask, jsonify
from flask_pymongo import PyMongo

from bson.json_util import dumps


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/academic_report"
mongo = PyMongo(app)

@app.route('/')
def studt():
    curser=mongo.db.marks.aggregate([{"$group": {"_id": "$name", "total": { "$sum": "$marks" }}}])
    d={}
    for i in curser:
        d[i["_id"]]=i["total"]
    #facl=mongo.db.faculty.find()
    return jsonify({"toptotal":min(d.items(),key=lambda x:x[1])})




if __name__=='__main__':
    app.run()
