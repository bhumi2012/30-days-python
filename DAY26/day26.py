# from flask import Flask, jsonify

# app = Flask(__name__)

# # Homepage
# @app.route("/")
# def home():
#     return "Welcome to Day 26: Python for Web!"

# # About route
# @app.route("/about")
# def about():
#     return "This is a simple Flask web app."

# # API route: list of students
# @app.route("/api/students")
# def get_students():
#     students = [
#         {"id": 1, "name": "Alice"},
#         {"id": 2, "name": "Bob"},
#         {"id": 3, "name": "Charlie"}
#     ]
#     return jsonify(students)

# if __name__ == "__main__":
#     app.run(debug=True)

# # http://127.0.0.1:5000/
# # http://127.0.0.1:5000/about
# # http://127.0.0.1:5000/api/students