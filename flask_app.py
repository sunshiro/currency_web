
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!!!!!!!!!!!'

@app.route('/aaaa')
def hello_world_aaaa():
    return 'the path is aaaa'

@app.route('/aaaa/bbbb')
def hello_world_aaaa_bbbb():
    return 'the path is aaaa/bbbb'
