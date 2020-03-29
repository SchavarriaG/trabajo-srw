from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    name = 'Sebaskendo'
    return render_template('index.html', name=name)


@app.route('/client')
def client():
    list_name = ['c1', 'c2', 'c3']
    return render_template('client.html', list=list_name)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
