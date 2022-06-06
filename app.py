from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'gitSimpExpvThree my-feature-branch Mon Jun  6 09:28:13 PDT 2022 says Hello, Docker!'
