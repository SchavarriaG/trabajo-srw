from flask import Flask
from flask import request

app = Flask(__name__) #nuevo objeto

@app.route('/') #wrap o un decorador
def index():
    return 'inicio' # Regresar un string


@app.route('/saluda')
def saluda():
    return'Holiwi' 


##params?params1=yuca&params2=papa
@app.route('/params')
def params():
    param = request.args.get('params1', 'no contiene este parametro')
    param2 = request.args.get('params2','no contiene este')
    return 'el parametro es : {}, {}'.format(param, param2)


if __name__ == '__main__':
    app.run( debug = True, port= 8000 ) #se encarga de ejecutar el servidor por el puerto 5000 en el localhost
