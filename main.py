# -*- encoding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request,redirect, url_for
from form import SignupForm
from form import LoginForm
from flask_login import LoginManager
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from models import users
from models import User
from models import get_user
from werkzeug.urls import url_parse
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from recommendation import recommen
import numpy as np
import math
import pandas as pd


app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

login_manager = LoginManager(app)
#login_manager.init_app(app)

conexion = MongoClient('mongodb+srv://inmanueld:securepass@ps4games-8q85r.mongodb.net/test?retryWrites=true&w=majority')
db = conexion.ps4

@app.route('/') 
def index():
    title = "index"
    return render_template('index.html', title=title)

@app.route('/signup/', methods=("GET", "POST"))
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('start'))
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        # Creamos el usuario y lo guardamos
        datos = {"nombre":str(name),"email":str(email),"password":str(password)}
        db.user.insert_one(datos)
        
        print(name)
        print(email)
        print(password)

        x = db.user.find_one({"email": str(email)})
        user = User(str(x.get('_id')),str(name),str(email),str(password))
        #user = User(len(users) + 1, name, email, password)
        #users.append(user)
        #print(users)

        # Dejamos al usuario logueado
        login_user(user, remember=True)
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('start')
        return redirect(next_page)
    return render_template("signup.html", form=form)


@login_manager.user_loader
def load_user(user_id):
    #for user in users:
     #   if user.id == int(user_id):
      #      return user
    #return None
    if db.user.find_one({"_id":ObjectId(str(user_id))}):
        x = db.user.find_one({"_id":ObjectId(str(user_id))})
      
        print("entra aca xd")
        
        return User(str(x.get('_id')),str(x.get('nombre')),str(x.get('email')),str(x.get('password')))
    print("entra aca NONE")
    return None

@app.route('/login/', methods=['GET', 'POST'])
def login():
    #print(current_user.is_authenticated)
    if current_user.is_authenticated:
        return redirect(url_for('start'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        print(user)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            print(current_user.is_authenticated)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('start')
            return redirect(next_page)
    return render_template('login_form.html', form=form)


@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index'))

def updateCal(title, email, cal):
    game = db.game2.find_one({ 'title': title })




@app.route('/start/<title>/<cal>/<info>')
@app.route('/start/')
def start(title=None, cal=None, info=None):
    user_r = db.user.find_one({"_id":ObjectId(str(current_user.get_id()))})
    email = user_r.get('email')
    name = user_r.get('nombre')
    if title != None:
        # updateCal(title, email, cal)
        print('Actualizando: ', title, cal, info)
        if info == '-1' or info == -1:
            up = db.game2.update_one({
                'title': title
                }, {'$push': {'rate': {'email': email, 'calificacion':cal} }})
            print(up)
        else:
            up = db.game2.update_one({ 'title': title, 'rate.email': email}, {'$set': { 'rate.$.calificacion' : cal }})
            print(up)
    Games = db.game2.find()
    Games2 = []
    calif = []
    for game in Games:
        rates = game['rate']
        flag = False
        for rate in rates:
            if rate['email'] == email:
                # calif.append(rate['calificacion'])
                game['rate2'] = rate['calificacion']
                flag = True
        if flag == False:
            game['rate2'] = '-1'
        Games2.append(game)
    return render_template('rate.html', list = Games2, email = email, name=name)

@app.route('/recomm/')
def recomm():
    user_r = db.user.find_one({"_id":ObjectId(str(current_user.get_id()))})
    list = recommen(user_r.get('email'))
    return render_template('recommendation.html',list = list)

if __name__ == '__main__':
    app.run( debug = True, port= 8000 ) 