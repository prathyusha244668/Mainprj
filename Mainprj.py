#Q1.Find the faculty with highest student count who got more than 90%.
from flask import Flask, jsonify
from flask_pymongo import PyMongo

from bson.json_util import dumps
from collections import defaultdict




app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/academic_report"
mongo = PyMongo(app)

@app.route('/hcnt')
def studt():
    curser = mongo.db.marks.find({"marks":{"$gt":90}})#curser is just like range fun to iterate here.and we got marks who got greater than 90 in evry sub for evry stu.
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

#Q2.Find the faculty with highest pass percentage (> 40%)
@app.route('/prsnt')
def prsnt():
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

    prsnt = {
    "Murali_Krishna": 0,
    "Amarnath": 0,
    "Samuel": 0,
    "Krishna_Reddy": 0,
    "Raja_Gopal": 0,
    "Ravi": 0
    }
    prsnt["Murali_Krishna"] = (di["Murali_Krishna"]/100)*100
    prsnt["Amarnath"] = (di["Amarnath"]/100)*100
    prsnt["Samuel"] = (di["Samuel"]/100)*100
    prsnt["Krishna_Reddy"] = (di["Krishna_Reddy"]/100)*100
    prsnt["Raja_Gopal"] = (di["Raja_Gopal"]/100)*100
    prsnt["Ravi"] = (di["Ravi"]/100)*100
    
    return jsonify({"$max":max(prsnt.items())})#key=lambda x:x[1])})


#Q3.Find the faculty with least pass percentage (<= 40%)
@app.route('/prcnt')
def prcent():
    curser = mongo.db.marks.find({"marks":{"$lte":40}})
    d= {
    "Murali_Krishna": 0,
    "Amarnath": 0,
    "Samuel": 0,
    "Krishna_Reddy": 0,
    "Raja_Gopal": 0,
    "Ravi": 0
    }

    for  i in curser:
        if i["subject"]=="Mathematics": 
            d["Murali_Krishna"] += 1
        if i["subject"] == "Telugu":
            d["Amarnath"] += 1
        if i["subject"] == "English":
            d["Samuel"] += 1
        if i["subject"] == "Social":
            d["Krishna_Reddy"] += 1
        if i["subject"] == "Physics":
            d["Raja_Gopal"] += 1
        if i["subject"] == "Chemistry":
            d["Ravi"] += 1

    prcent = {
    "Murali_Krishna": 0,
    "Amarnath": 0,
    "Samuel": 0,
    "Krishna_Reddy": 0,
    "Raja_Gopal": 0,
    "Ravi": 0
    }
    prcent["Murali_Krishna"] = (d["Murali_Krishna"]/100)*100
    prcent["Amarnath"] = (d["Amarnath"]/100)*100
    prcent["Samuel"] = (d["Samuel"]/100)*100
    prcent["Krishna_Reddy"] = (d["Krishna_Reddy"]/100)*100
    prcent["Raja_Gopal"] = (d["Raja_Gopal"]/100)*100
    prcent["Ravi"] = (d["Ravi"]/100)*100
    
    return jsonify({"$min":min(prcent.items())})#key=lambda x:x[1])})



#Q4.Who is the top student with maximum total?
@app.route('/top')
def studnt():
    curser=mongo.db.marks.aggregate([{"$group": {"_id": "$name", "total": { "$sum": "$marks" }}}])
    d={}
    for i in curser:
        d[i["_id"]]=i["total"]
    #facl=mongo.db.faculty.find()
    return jsonify({"toptotal":max(d.items(),key=lambda x:x[1])})

#Q5.Who is the best student in Mathematics?
@app.route('/best')
def bst():
    cursor =mongo.db.marks.find({ "$and":[{"subject": "Mathematics"},{"marks":{"$gt":90}}]})

    b={}
    for i in cursor:
        if i["subject"] not in b:
            b[i["name"]]=i["marks"]
    
    return jsonify({"best":max(b.items(),key=lambda x:x[1])})

#Q6.What is the average mark for each subject, (ignore failures)?
@app.route('/avg')
def avrg():      
    curser=mongo.db.marks.find({"marks":{"$gt":40}})

    d=defaultdict(list)
    for i in curser:
        d[i["subject"]].append(i["marks"]) 

    b={}
    for i ,c in d.items():
        s=0
        for j in c:
            s=s+j
        b[i]=(s/len(c))
    
        
    #facl=mongo.db.faculty.find()'''

    return jsonify({"avg":b})

#Q7.Find the student with least numbers of marks as total.def student():
@app.route('/least')
def student():
    curser=mongo.db.marks.aggregate([{"$group": {"_id": "$name", "total": { "$sum": "$marks" }}}])
    d={}
    for i in curser:
        d[i["_id"]]=i["total"]
    #facl=mongo.db.faculty.find()
    return jsonify({"toptotal":min(d.items(),key=lambda x:x[1])})




if __name__=='__main__':
    app.run(debug=True)






