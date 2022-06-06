from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'gitSimpExpvThree main Mon Jun  6 09:12:01 PDT 2022 says Hello, Docker!'
