# -*- encoding: utf-8 -*-
import pymongo
 
from pymongo import MongoClient
 
# conexión
con = MongoClient('mongodb+srv://inmanueld:securepass@ps4games-8q85r.mongodb.net/test?retryWrites=true&w=majority')

#my db
db = con.ps4
 
# colección
User = db.game

db.game.update_one({'title': 'Borderlands 3'}, {'$push': {'rate': {'email': 'hotboy@gmail.com', 'calificacion':'5'} }})
db.game.update_one({'title': 'Doom Eternal'}, {'$push': {'rate': {'email': 'hotboy@gmail.com', 'calificacion':'5'} }}) 
db.game.update_one({'title': 'Crash Team Racing Nitro-Fueled'}, {'$push': {'rate': {'email': 'hotboy@gmail.com', 'calificacion':'5'} }})
db.game.update_one({'title': 'Resident Evil 3 with Pre-Order Bonus DLC'}, {'$push': {'rate': {'email': 'hotboy@gmail.com', 'calificacion':'3'} }})
db.game.update_one({'title': "Assassin's Creed 3 Remastered"}, {'$push': {'rate': {'email': 'hotboy@gmail.com', 'calificacion':'4'} }})
db.game.update_one({'title': 'AFL Evolution 2'}, {'$push': {'rate': {'email': 'hotboy@gmail.com', 'calificacion':'2'} }})
db.game.update_one({'title': 'Legendary Fishing'}, {'$push': {'rate': {'email': 'hotboy@gmail.com', 'calificacion':'1'} }})
db.game.update_one({'title': "Space Junkies"}, {'$push': {'rate': {'email': 'hotboy@gmail.com', 'calificacion':'5'} }})
db.game.update_one({'title': "Tom Clancy's Ghost Recon: Wildlands Gold Edition"}, {'$push': {'rate': {'email': 'hotboy@gmail.com', 'calificacion':'5'} }})
db.game.update_one({'title': "Final Fantasy VII Remake with Pre-Order Bonus DLC"}, {'$push': {'rate': {'email': 'hotboy@gmail.com', 'calificacion':'1'} }})


#resultado = User.find()
 
#for x in resultado:}
# 	print(x)
 
#insert
#datos = { "nombre": "juanito", "email": "bigdaddy@gmail.com", "password": "789456"}


#x = User.insert_one(datos) 
#print(x)
