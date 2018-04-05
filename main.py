from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/welcome")
def welcome():
    return render_template('welcome.html')

@app.route("/")
def index():
    return render_template('index.html')

app.run()
