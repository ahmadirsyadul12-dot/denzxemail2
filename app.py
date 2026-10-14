from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "zhen-email OK - login: datpol / 123456"

@app.route('/app.py')
def same():
    return home()
