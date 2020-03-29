from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/user/<name>')
def user(name='default'):
    age = 23
    list = [1,2,3,4]
    return render_template('user.html', namehtml = name, agehtml = age, listhtml = list)

if __name__ == '__main__':
    app.run( debug = True, port= 8000 )