from flask import Flask, jsonify
from flask_pymongo import PyMongo

from bson.json_util import dumps


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/academic_report"
mongo = PyMongo(app)

@app.route('/')
def studt():
    curser = mongo.db.marks.find({"marks":{"$gt":90}})
    curser1=mongo.db.faculty.find()
    c1={}
    for i in curser:
        if i["subject"] not in c1:
            c1[i["subject"]]=1
        else:
            c1[i["subject"]]+=1
    count=max(c1.items(),key=lambda x: x[1])
    for j in curser1:
        if count[0]==j["name"]:
            return jsonify({"fac":j["subject"]})#key=lambda x: x[1]})
            

if __name__=='__main__':
    app.run(debug=True)












