from flask import Flask 
app = Flask(__name__)
@app.route('/')
def home():
    return "<p> Mignonne, allons voir si la rose </p>"
