# -*- encoding: utf-8 -*-
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

# conexión
con = MongoClient('mongodb+srv://inmanueld:securepass@ps4games-8q85r.mongodb.net/test?retryWrites=true&w=majority')

#my db
db = con.ps4
 
# colección
User = db.user

db.user


myquery = { "email": "hotboy@gmail.com" }

mydoc = db.user.find(myquery)

#x = "tigre"
#if db.user.find_one({"email": "hotboyy@gmail.com"}):
 #   x = "yuca"
y = 'hotboy@gmail.com'
z = ObjectId('5e80cd22c84c50a8332555da')
print(type(z))
w = "5e80cd22c84c50a8332555da"
x = db.user.find_one({"_id": z })
print(x)
print(x.get('_id'))



word = "yuca"
word2 = "yuac"

if word == word2:
    print("yes")
else:
    print("Nel mijo")


#for y in x:
 # print(y.get('_id')) 

#db.game.update_one({'title': "Final Fantasy VII Remake with Pre-Order Bonus DLC"}, {'$push': {'rate': {'email': 'hotboy@gmail.com', 'calificacion':'1'} }})


#resultado = User.find()
 
#for x in resultado:}
# 	print(x)
 
#insert
#datos = { "nombre": "juanito", "email": "bigdaddy@gmail.com", "password": "789456"}


#x = User.insert_one(datos) 
#print(x)
