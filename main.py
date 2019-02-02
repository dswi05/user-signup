from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=['POST'])
def add_user():
    new_user = request.form['new-user']

@app.route("/", methods=['POST'])
def password():
    pswd = request.form['set-pswd']

@app.route("/", methods=['POST'])
def verify_password():
    verify_pswd = request.form['verify-pswd']

@app.route("/", methods=['POST'])
def email():
    set_email = request.form['set-email']

@app.route("/")
def index():
    return render_template('index.html')

app.run()