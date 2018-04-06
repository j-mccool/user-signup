from flask import Flask, request, redirect, render_template
import cgi
import re

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/welcome", methods=['POST'])
def welcome():
    new_user = request.form['username']
    password = request.form['password']
    password_confirm = request.form['password_confirm']
    email = request.form['email']

    u_error = ''
    p_error = ''
    pc_error = ''
    e_error = ''

    #name validation
    regex_contains = r"([\s])" 
    #regex_email = r"([\w\-_]+)?\w+@{1}[\w]+\.{1}\w+"

    def email_check(x):
        y = 0

        if x.count(' ') > 0:
            y += 1
        elif x.count('@') != 1:
            y += 1
        elif x.count('.') != 1:
            y += 1
        if y > 0:
            return True

    if re.search(regex_contains, new_user):
        u_error = "Username can't contain spaces. Please re-enter."
    if re.search(regex_contains, password):
        p_error = "Password cannot contain spaces. Please re-enter."
    if len(password) > 20 or len(password) < 3:
        p_error = "Invalid password. Must be between 3 and 20 characters."
    if len(new_user) > 20 or len(new_user) < 3:
        u_error = "Invalid username. Must be between 3 and 20 characters."
    if new_user == '':
        u_error = "That's not a valid username. Value must not be null."
    if password == '':
        p_error = "Invalid password. Cannot be null."
    if password_confirm != password:
        pc_error = "Passwords must match. Please re-enter."
    if email:
            if re.search(regex_contains, email):
                e_error = "Email cannot contain spaces. Please re-enter."
            #if not re.search(regex_email, email):
            #    e_error = "Email must contain a single \'.\' and a single \'@\'. Please re-enter."
            if email_check(email):
                e_error = "Email must contain a single \'.\' and a single \'@\'. Please re-enter."
            if len(email) > 20 or len(email) < 3:
                e_error = "Email must be between 3 and 20 charactesr. Please re-enter."

    if not u_error and not p_error and not pc_error and not e_error:
        return render_template('welcome.html', username = new_user)
    else:
        return render_template('index.html', username = new_user, u_error=u_error, p_error = p_error, pc_error = pc_error, email = email, e_error = e_error)



    return render_template('welcome.html', username = new_user)

@app.route("/")
def index():
    return render_template('index.html')

app.run()
