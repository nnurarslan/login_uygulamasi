import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["users_db"]
collection = db["users"]
def add_users(username, password):
    user_data = {
        "username": username,
        "password": password
    }
    collection.insert_one(user_data)
    print("bilgiler eklendi")

username = input("Kullanıcı adını giriniz")
password = input("Şifre giriniz")
add_users(username,password)