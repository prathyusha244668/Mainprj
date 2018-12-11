#Q1.Find the faculty with highest student count who got more than 90%.

from flask import Flask, jsonify
from flask_pymongo import PyMongo

from bson.json_util import dumps
from collections import defaultdict




app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/academic_report"
mongo = PyMongo(app)

@app.route('/highestcount')
def studt():
    curser = mongo.db.marks.find({"marks":{"$gt":90}})#curser is just like range fun to iterate here.and we got marks who got greater than 90 in evry subj for evry stu.
    curser1=mongo.db.faculty.find()#fac_name,fac_subj will b thr.
    c1={}
    for i in curser:
        if i["subject"] not in c1:#calculating subject count who got abv 90 
            c1[i["subject"]]=1
        else:
            c1[i["subject"]]+=1
    count=max(c1.items(),key=lambda x: x[1])#convrtng dict to list to tuples to get max count..using lambda for considering  subj count..
    for j in curser1:
        if count[0]==j["name"]:#here count[0] refers to subject name(eng)in count &  j[name] means subject name(eng) in faculty.
            
            return jsonify({"fac":j["subject"]})#key=lambda x: x[1]})#we have max value in count that is english with 11..compared sub names(eng) abv..if it is matched ,faculty name(samul) of that subj will b returned.








#Q2.Find the faculty with highest pass percentage (> 40%)

@app.route('/highestprsnt')
def prsent():
    curser = mongo.db.marks.find({"marks":{"$gt":40}})#marks who got greater than 40
    di= {
    "Murali_Krishna": 0,
    "Amarnath": 0,
    "Samuel": 0,
    "Krishna_Reddy": 0,
    "Raja_Gopal": 0,#  creating dict & assigning faculty names with 0 value    
   
    "Ravi": 0
    }
    for i in curser:
        if i["subject"]=="Mathematics": #calculating  subj(Mathematics) total .evry stu who got more than 40 
          di["Murali_Krishna"]+=i["marks"]# & assigning total to fac_name of that particular subj.
        if i["subject"] == "Telugu":
            di["Amarnath"] += i["marks"]
        if i["subject"] == "English":
            di["Samuel"] += i["marks"]
        if i["subject"] == "Social":#calculating  subj(social) total .evry stu who got more than 40
            di["Krishna_Reddy"] += i["marks"]# & assigning total to fac_name of that particular subj.
        if i["subject"] == "Physics":
            di["Raja_Gopal"] += i["marks"]
        if i["subject"] == "Chemistry":
            di["Ravi"] += i["marks"]

    prsnt={}#empty dict
    prsnt["Murali_Krishna"] = di["Murali_Krishna"]/100#d[key]=(prsnt["Murali_Krishna"])  #we got subj total above(di["fac_name"]) and calculating percentage.
    prsnt["Amarnath"] = (di["Amarnath"]/100)
    prsnt["Samuel"] = (di["Samuel"]/100)
    prsnt["Krishna_Reddy"] = (di["Krishna_Reddy"]/100)
    prsnt["Raja_Gopal"] = (di["Raja_Gopal"]/100)
    prsnt["Ravi"] = (di["Ravi"]/100)
    
    return jsonify({"$max":max(prsnt.items(),key=lambda x:x[1])})#convrtng dict to list to tuples to get max percentg..using lambda fun for considering  percentage 









#Q3.Find the faculty with least pass percentage (<= 40%)

@app.route('/leastprcnt')
def prcent():
    curser = mongo.db.marks.find({"marks":{"$gt":40}})#marks who got greater than 40
    di= {
    "Murali_Krishna": 0,
    "Amarnath": 0,
    "Samuel": 0,
    "Krishna_Reddy": 0,
    "Raja_Gopal": 0,
    "Ravi": 0
    }#  creating dict & assigning faculty names with 0 value    
   
    
    for  i in curser:
        if i["subject"]=="Mathematics": #calculating  subj(Mathematics) total .evry stu who got more than 40 
          di["Murali_Krishna"]+=i["marks"]# & assigning total to fac_name of that particular subj.
        if i["subject"] == "Telugu":
            di["Amarnath"] += i["marks"]
        if i["subject"] == "English":
            di["Samuel"] += i["marks"]
        if i["subject"] == "Social":
            di["Krishna_Reddy"] += i["marks"]
        if i["subject"] == "Physics":#calculating  subj(physics) total .evry stu who got more than 40
            di["Raja_Gopal"] += i["marks"]# & assigning total to fac_name of that particular subj.
        if i["subject"] == "Chemistry":
            di["Ravi"] += i["marks"]

    prcnt={}
    prcnt["Murali_Krishna"] = di["Murali_Krishna"]/100#d[key]=(prsnt["Murali_Krishna"])  #we got subj total above(di["fac_name"]) and calculating percentage.
    prcnt["Amarnath"] = (di["Amarnath"]/100)
    prcnt["Samuel"] = (di["Samuel"]/100)
    prcnt["Krishna_Reddy"] = (di["Krishna_Reddy"]/100)
    prcnt["Raja_Gopal"] = (di["Raja_Gopal"]/100)
    prcnt["Ravi"] = (di["Ravi"]/100)
    
    return jsonify({"$min":min(prcnt.items(),key=lambda x:x[1])})#convrtng dict to list to tuples to get max percentg..using lambda fun for considering  percentage 









#Q4.Who is the top student with maximum total?

@app.route('/topstudent')
def studnt():
    curser=mongo.db.marks.aggregate([{"$group": {"_id": "$name", "total": { "$sum": "$marks" }}}])#using aggregate  method .we are  grouping name and total for calculating  SUM.
    d={}
    for i in curser:
        d[i["_id"]]=i["total"]#assigning student names as 'key' and there total total as 'value'.

    return jsonify({"topstutot":max(d.items(),key=lambda x:x[1])})#convrtng dict to list to tuples to get max total..using lambda fun for considering total..or else it will consider stu names for max fun.









#Q5.Who is the best student in Mathematics?

@app.route('/beststudent')
def best():
    cursor =mongo.db.marks.find({ "$and":[{"subject": "Mathematics"},{"marks":{"$gt":90}}]})#using 'and' we are combining subject("Mathematics")and marks..here we got marks who got greater than 90 for finding top stu.

    b={}
    for i in cursor:
        if i["subject"] not in b:#condition: subj mathematics not in b(empty) 
            b[i["name"]]=i["marks"]#i[name] is stu name as 'key' and i['marks] is stu marks of maths subj..as 'value'
    
    return jsonify({"beststu":max(b.items(),key=lambda x:x[1])})#convrtng dict to list to tuples to get max marks as best stu..using lambda fun for considering marks










#Q6.What is the average mark for each subject, (ignore failures)?

@app.route('/avg')
def avrg():      
    curser=mongo.db.marks.find({"marks":{"$gt":40}})#got marks who got greater than 40 

    d=defaultdict(list)#default dict passing list as parameter
    for i in curser:
        d[i["subject"]].append(i["marks"]) #appending list of marks who got more than 40 to that particular subjects.

    b={}
    for i ,c in d.items():#d.items() will convrt to list to tuples ..we have subjects  as 'i ' here,and list of marks grtr than 40 as 'c' here..
        s=0#sum=0
        for j in c:#taking each mark as j in c(list of marks)
            s=s+j #adding evry mark from list of marks of each subj
        b[i]=(s/len(c))# here  b[i] is subject name and calculating avrg by divding each subj total by length of c(list of marks)

    return jsonify({"avg mark":b})#b (avrg)







#Q7.Find the student with least numbers of marks as total.def student():

@app.route('/leasttotal')
def student():
    curser=mongo.db.marks.aggregate([{"$group": {"_id": "$name", "total": { "$sum": "$marks" }}}])#using aggregate  method .we are  grouping name and total for calculating  SUM.
    d={}
    for i in curser:
        d[i["_id"]]=i["total"]#assigning student names as 'key' and there total total as 'value'.
    
    return jsonify({"leasttot":min(d.items(),key=lambda x:x[1])})#convrtng dict to list to tuples to get minimum total..using lambda fun for considering total.




if __name__=='__main__':
    app.run(debug=True)






