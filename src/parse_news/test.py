from pymongo import MongoClient


client = MongoClient()
db = client["parse_habr"]
collection = db["habr_python"]

client.drop_database("parse_habr")