from pymongo import MongoClient

# Replace with your MongoDB connection string
client = MongoClient("mongodb://localhost:27017")
db = client.student_database
