from flask import Flask, jsonify
from flask_pymongo import PyMongo

from bson.json_util import dumps
from collections import defaultdict


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/academic_report"
mongo = PyMongo(app)

@app.route('/avrg')
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



if __name__=='__main__':
    app.run()



'''
Mathematics = []
Telugu = []
English = []
Social = []
Physics = []
Chemistry = []

def my_function(sub):
    if sub == "Mathematics":
        Mathematics.append(int(line[2]))
    if sub == "Telugu":
        Telugu.append(int(line[2]))
    if sub == "English":
        English.append(int(line[2]))
    if sub == "Social":
        Social.append(int(line[2]))
    if sub == "Physics":
        Physics.append(int(line[2]))
    if sub == "Chemistry":
        Chemistry.append(int(line[2]))


with open("student_marks.csv", "r") as fp:
    data = csv.reader(fp, delimiter=',')
    for line in data:
        if int(line[2]) >= 36:
            my_function(line[1])

print("Average in Mathematics : " + str(sum(Mathematics)/len(Mathematics)))
print("Average in Telugu : " + str(sum(Telugu)/len(Telugu)))
print("Average in English : " + str(sum(English)/len(English)))
print("Average in Social : " + str(sum(Social)/len(Social)))
print("Average in Physics : " + str(sum(Physics)/len(Physics)))
print("Average in Chemistry : " + str(sum(Chemistry)/len(Chemistry)))'''