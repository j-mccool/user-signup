from flask import Flask, request, redirect, render_template
import cgi

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
    if new_user == '':
        u_error = "That's not a valid username. Value must not be null."
    if password == '':
        p_error = "Invalid password. Cannot be null."
    if len(password) < 3:
        p_error = "Invalid password. Must be between 3 and 20 characters, and cannot contain spaces."
    elif len(password) > 20:
        p_error = "Invalid password. Must be between 3 and 20 characters, and cannot contain spaces."
    elif " " in password:
        p_error = "Invalid password. Passwords cannot contain spaces."
    if password_confirm == '':
        pc_error = "Password confirmation must match password entered above. Please try again."
    if password_confirm != password:
        pc_error = "Password and Confirmation must match. Please try again."
    if email:
        if len(email) < 3:
            e_error = "Email must be between 3 and 20 characters."
        if len(email) > 20:
            e_error = "Email must be between 3 and 20 characters."
        if email.count(".") != 1:
            e_error = "Email must contain a single \'.\' and a single \'@\'. Please re-enter."
        elif email.count("@") !=1:
            e_error = "Email must contain a single \'.\' and a single \'@\'. Please re-enter."
        if " " in email:
            e_error = "Email cannot contain a space. Please re-enter."

    if not u_error and not p_error and not pc_error and not e_error:
        return render_template('welcome.html', username = new_user)
    else:
        return render_template('index.html', username = new_user, u_error=u_error, p_error = p_error, pc_error = pc_error, email = email, e_error = e_error)



    return render_template('welcome.html', username = new_user)

@app.route("/")
def index():
    return render_template('index.html')

app.run()
