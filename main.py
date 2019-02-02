from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html', new_user="", user_error="")

@app.route("/", methods=['POST'])
def add_user():

    new_user = request.form['new-user']
    user_error = ""
    if len(new_user) < 3:
        user_error = "User name must be greater than two characters."
        new_user = ""
    elif len(new_user) > 20:
        user_error = "User name must be less than twenty characters."
        new_user = ""
    for char in new_user:
        if char == " ":
            user_error = "User name cannot contain spaces."
            new_user = ""

    pswd = request.form['set-pswd']
    password_error = ""
    if len(pswd) < 3:
        password_error = "Password must be greater than two characters."
        pswd = ""
    elif len(pswd) > 20:
        password_error = "Password must be less than twenty characters."
        pswd = ""
    for char in pswd:
        if char == " ":
            password_error = "Password cannot contain spaces."
            pswd = ""

    verify_pswd = request.form['verify-pswd']
    verify_error = ""
    if verify_pswd != pswd:
        verify_error = "Password does not match."
        verify_pswd = ""

    set_email = request.form['new-email']
    email_error = ""
    if "." not in set_email:
        email_error = "Email must contain '@' and '.' symbols."
        set_email = ""
    elif "@" not in set_email:
        email_error = "Email must contain '@' and '.' symbols."
        set_email = ""
    elif len(set_email) <3:
        email_error = "Email must be greater than three characters."
        set_email = ""
    elif len(set_email) >20:
        email_error = "Email must be less than twenty characters."
        set_email = ""
    for char in set_email:
        if char == " ":
            email_error = "Email cannot contain spaces."
            set_email = ""
    
    if not user_error and not password_error and not verify_error and not email_error:
        return render_template("welcome.html", new_user=new_user)
    else:
        return render_template('index.html', new_user=new_user, set_email=set_email, user_error=user_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

    # if not user_error:
    #     if not password_error:
    #         if not verify_error:
    #             if not email_error:
    #                 return render_template('welcome.html', new_user=new_user)
    #             else: return render_template('index.html', new_user=new_user, set_email=set_email, user_error=user_error, password_error=password_error, verify_error=verify_error, email_error=email_error)
    #         else:
    #             return render_template('index.html', new_user=new_user, set_email=set_email, user_error=user_error, password_error=password_error, verify_error=verify_error)
    #     else:
    #         return render_template('index.html', new_user=new_user, set_email=set_email, user_error=user_error, password_error=password_error)
    # else:
    #     return render_template('index.html', new_user=new_user, set_email=set_email, user_error=user_error)

app.run()