# only for practice purpose

# from flask import Flask,  Response 
# import json 
# import os

# app = Flask(__name__) 
 
# @app.route('/api/v1.0/students', methods = ['GET']) 
# def students (): 
#     student_list = [ 
#         { 
#             'name':'Asabeneh', 
#             'country':'Finland', 
#             'city':'Helsinki', 
#             'skills':['HTML', 'CSS','JavaScript','Python'] 
#         }, 
#         { 
#             'name':'David', 
#             'country':'UK', 
#             'city':'London', 
# 'skills':['Python','MongoDB'] 
# }, 
# { 
# 'name':'John', 
# 'country':'Sweden', 
# 'city':'Stockholm', 
# 'skills':['Java','C#'] 
# } 
# ] 
#     return Response(json.dumps(student_list), 
# mimetype='application/json') 
# if __name__ == '__main__': 
# # for deployment 
# # to make it work for both production and development 
#  port = int(os.environ.get("PORT", 5000)) 
#  app.run(debug=True, host='0.0.0.0', port=port)


# http://127.0.0.1:5000/api/v1.0/students


 
# from flask import Flask,  Response 
# import json 
# import pymongo 
# import os
 
 
# app = Flask(__name__) 
 
# # 
# MONGODB_URI = "mongodb+srv://bhumi20:bhumiimodi.20@30daysofpython.isr1trn.mongodb.net/?retryWrites=true&w=majority&appName=30daysofpython"
# client = pymongo.MongoClient(MONGODB_URI) 
# db = client['thirty_days_of_python'] # accessing the database 
 
# @app.route('/api/v1.0/students', methods = ['GET']) 
# def students (): 
 
#     return Response(json.dumps(students), 
# mimetype='application/json') 
 
 
# if __name__ == '__main__': 
#     # for deployment 
#     # to make it work for both production and development 
#     port = int(os.environ.get("PORT", 5000)) 
# app.run(debug=True, host='0.0.0.0', port=port) 


# new exmple

# from flask import Flask, Response, request
# import json
# from bson.objectid import ObjectId
# from bson.json_util import dumps
# import pymongo
# from datetime import datetime
# import os

# app = Flask(__name__)

# # MongoDB connection
# MONGODB_URI = "mongodb+srv://bhumi20:bhumiimodi.20@30daysofpython.isr1trn.mongodb.net/?retryWrites=true&w=majority&appName=30daysofpython"
# client = pymongo.MongoClient(MONGODB_URI)
# db = client['thirty_days_of_python']
# students_collection = db['students']


# # ---------- ROUTES ----------

# # Seed route - insert sample students
# @app.route('/api/v1.0/seed', methods=['GET'])
# def seed_data():
#     students_collection.insert_many([
#         {
#             "name": "Asabeneh",
#             "country": "Finland",
#             "city": "Helsinki",
#             "skills": ["HTML", "CSS", "JavaScript", "Python"],
#             "bio": "Educator and developer",
#             "birthyear": 1980,
#             "created_at": datetime.now()
#         },
#         {
#             "name": "David",
#             "country": "UK",
#             "city": "London",
#             "skills": ["Python", "MongoDB"],
#             "bio": "Backend Developer",
#             "birthyear": 1990,
#             "created_at": datetime.now()
#         }
#     ])
#     return Response(dumps({"result": "Sample students added"}), mimetype='application/json')


# # GET all students
# @app.route('/api/v1.0/students', methods=['GET'])
# def get_students():
#     students = list(students_collection.find({}, {"_id": 0}))  # exclude _id for cleaner JSON
#     return Response(json.dumps(students), mimetype='application/json')


# # GET single student by ID
# @app.route('/api/v1.0/students/<id>', methods=['GET'])
# def get_single_student(id):
#     student = students_collection.find_one({'_id': ObjectId(id)})
#     return Response(dumps(student), mimetype='application/json')


# # POST create student
# @app.route('/api/v1.0/students', methods=['POST'])
# def create_student():
#     name = request.form['name']
#     country = request.form['country']
#     city = request.form['city']
#     skills = request.form['skills'].split(', ')
#     bio = request.form['bio']
#     birthyear = request.form['birthyear']
#     created_at = datetime.now()

#     student = {
#         'name': name,
#         'country': country,
#         'city': city,
#         'birthyear': birthyear,
#         'skills': skills,
#         'bio': bio,
#         'created_at': created_at
#     }
#     students_collection.insert_one(student)
#     return Response(dumps({"result": "Student created"}), mimetype='application/json')


# # PUT update student
# @app.route('/api/v1.0/students/<id>', methods=['PUT'])
# def update_student(id):
#     query = {"_id": ObjectId(id)}

#     name = request.form['name']
#     country = request.form['country']
#     city = request.form['city']
#     skills = request.form['skills'].split(', ')
#     bio = request.form['bio']
#     birthyear = request.form['birthyear']
#     created_at = datetime.now()

#     student = {
#         'name': name,
#         'country': country,
#         'city': city,
#         'birthyear': birthyear,
#         'skills': skills,
#         'bio': bio,
#         'created_at': created_at
#     }

#     students_collection.update_one(query, {"$set": student})
#     return Response(dumps({"result": "Student updated"}), mimetype='application/json')


# # DELETE student
# @app.route('/api/v1.0/students/<id>', methods=['DELETE'])
# def delete_student(id):
#     students_collection.delete_one({"_id": ObjectId(id)})
#     return Response(dumps({"result": "Student deleted"}), mimetype='application/json')


# # ---------- START APP ----------
# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)


# # insert sample  http://127.0.0.1:5000/api/v1.0/seed
