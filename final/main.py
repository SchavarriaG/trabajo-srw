from flask import Flask
from flask import render_template
from flask import request,redirect, url_for
from form import SignupForm
from form import LoginForm
from flask_login import LoginManager
from flask_login import current_user
from flask_login import login_user
from models import users
from models import User
from models import get_user
from werkzeug.urls import url_parse
import pymongo
from pymongo import MongoClient




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
        return redirect(url_for('index'))
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
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("signup.html", form=form)


@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('login_form.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run( debug = True, port= 8000 ) 