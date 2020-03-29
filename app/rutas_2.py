from flask import Flask
from flask import request

app = Flask(__name__)  

@app.route('/')  
def index():
    return 'inicio'  

@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>')
def params(name = 'default', num = 'nada'):
    return 'el parametro es : {} {}'.format(name,num)

if __name__ == '__main__':
    # se encarga de ejecutar el servidor por el puerto 5000 en el localhost
    app.run(debug=True, port=8000)
