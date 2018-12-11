from flask import Flask, jsonify, request
import json
from flask_pymongo import PyMongo

from flask import request

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/academic_report"
mongo = PyMongo(app)



@app.route('/newf', methods=['put'])
def poste():
    data=request.get_json()
    doc1 = data["doc1"]
    doc2 = data["doc2"]
    doc3 = data["doc3"]
    
    mongo.db.test.update_many({"doc1":{"Subject":"flask"}, "doc2":{"Subject":"flask"},"doc3":{"Subject":"jvsrpt"}})
    
    
    #mongo.db.test.update({"$marks":{"$gt":90}},{"$set":{"Subject":"jsvsrpt"}})
    #mongo.db.test.update({"$marks":{"$gt":50}},{"$set":{"Subject":"nodejs" }})
    #mongo.db.test.update({"$marks":{"$gt":70}},{"$set":{"Subject":"flask" }})


    #mongo.db.test.insert_many([doc1])
    #new_en = mongo.db.pattu.find_one({'_id': n_id })
    #output = {'doc1' : new_en['doc1'], 'doc2' : new_en['doc2']}
    return jsonify({'result' : "success"})

if __name__=='__main__':
    app.run()
