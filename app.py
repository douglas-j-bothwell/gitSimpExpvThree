from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'gitSimpExpMay31 initial-setup says Hello, Docker!'
