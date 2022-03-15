from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>hello, world<h1>'


app.run(host='0.0.0.0')
