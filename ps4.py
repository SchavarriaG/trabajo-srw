# -*- encoding: utf-8 -*-
import pymongo
 
from pymongo import MongoClient
 
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
x = db.user.find_one({"email": "hotboy@gmail.com"})
print(x.get('_id'))

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
