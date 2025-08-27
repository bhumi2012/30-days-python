# example

# import pymongo

# MONGODB_URI = "mongodb+srv://bhumi20:bhumiimodi.20@30daysofpython.isr1trn.mongodb.net/?retryWrites=true&w=majority&appName=30daysofpython"

# client = pymongo.MongoClient(MONGODB_URI)

# try:
#     print("Databases:", client.list_database_names())
# except Exception as e:
#     print("Connection failed:", e)


# import pymongo

# MONGODB_URI = "mongodb+srv://bhumi20:bhumiimodi.20@30daysofpython.isr1trn.mongodb.net/?retryWrites=true&w=majority"

# client = pymongo.MongoClient(MONGODB_URI)

# db = client["testdb"]        # create/use a database
# collection = db["users"]     # create/use a collection

# # Insert one document
# collection.insert_one({"name": "Bhumi", "age": 22})

# print("Inserted successfully!")
# print("All users:", list(collection.find()))

# example

# import pymongo

# MONGODB_URI = "mongodb+srv://bhumi20:bhumiimodi.20@30daysofpython.isr1trn.mongodb.net/?retryWrites=true&w=majority"

# try:
#     client = pymongo.MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
#     client.server_info()  
#     print(" MongoDB Connected!")
    
#     # Example query
#     db = client["school"]
#     students = db["students"]
#     students.insert_one({"name": "Amit", "grade": "A"})
#     print("Data inserted into 'school.students'")
# except Exception as e:
#     print(" Connection failed:", e)




