# -*- encoding: utf-8 -*-
import pymongo
 
from pymongo import MongoClient
 
# conexión
con = MongoClient('mongodb+srv://inmanueld:securepass@ps4games-8q85r.mongodb.net/test?retryWrites=true&w=majority')
db = con.ps4
 
# colección
User = db.user
 
# resultado = cuentas.find()
 
# for x in resultado:
# 	print(x)
 
# insert
datos = { "nombre": "Alejandro Martínez", "ciudad": "Bogotá DC" }

x = User.insert_one(datos)
print(x)