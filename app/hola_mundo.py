from flask import Flask


app = Flask(__name__) #nuevo objeto

@app.route('/') #wrap o un decorador
def index():
    return('Hola mundo') # Regresar un string

app.run() #se encarga de ejecutar el servidor por el puerto 5000 en el localhost