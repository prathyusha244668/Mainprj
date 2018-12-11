from flask import Flask, jsonify
from flask_pymongo import PyMongo

from bson.json_util import dumps


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/academic_report"
mongo = PyMongo(app)

@app.route('/')
def prcnt():
    curser = mongo.db.marks.find({"marks":{"$gt":40}})
    di= {
    "Murali_Krishna": 0,
    "Amarnath": 0,
    "Samuel": 0,
    "Krishna_Reddy": 0,
    "Raja_Gopal": 0,
    "Ravi": 0
    }

    for  i in curser:
        if i["subject"]=="Mathematics": 
            di["Murali_Krishna"] += 1
        if i["subject"] == "Telugu":
            di["Amarnath"] += 1
        if i["subject"] == "English":
            di["Samuel"] += 1
        if i["subject"] == "Social":
            di["Krishna_Reddy"] += 1
        if i["subject"] == "Physics":
            di["Raja_Gopal"] += 1
        if i["subject"] == "Chemistry":
            di["Ravi"] += 1

    prcnt = {
    "Murali_Krishna": 0,
    "Amarnath": 0,
    "Samuel": 0,
    "Krishna_Reddy": 0,
    "Raja_Gopal": 0,
    "Ravi": 0
    }
    prcnt["Murali_Krishna"] = (di["Murali_Krishna"]/100)*100
    prcnt["Amarnath"] = (di["Amarnath"]/100)*100
    prcnt["Samuel"] = (di["Samuel"]/100)*100
    prcnt["Krishna_Reddy"] = (di["Krishna_Reddy"]/100)*100
    prcnt["Raja_Gopal"] = (di["Raja_Gopal"]/100)*100
    prcnt["Ravi"] = (di["Ravi"]/100)*100
    
    return jsonify({"$max":max(prcnt.items())})#key=lambda x:x[1])})








if __name__=='__main__': 
    app.run()


