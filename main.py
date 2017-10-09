from flask import Flask, request, render_template



app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])
def display_user_form():
    return user_form.format(username='', un_error='', 
    password ='', pw_error='', verifypw='', vpw_error='') 



@app.route('/', methods=['POST'])
def user_validation():
    username = request.form["username"]
    password = request.form["password"]
    verify_pw = request.form["verifypw"]
    email = request.form["email"]

    un_error = ""
    pw_error = ""
    vpw_error = ""
    email_error = ""


    if username == "" or " " in username or len(username) < 3 or len(username) > 20:
         un_error = "Not a valid Username"    
    
    if password == "" or " " in username or len(username) < 3 or len(username) > 20:
        pw_error = "Not a valid Password"
    
    if verify_pw == "" or verify_pw != password:
        vpw_error = "Passwords do not match"

    if email != "":
        if "@" not in email or "." not in email or " " in email or len(email) < 3 or len(email) > 20:
            email_error = "Invalid email"

    if email_error == "" and un_error == "" and pw_error == "" and vpw_error == "":
        return render_template("welcome.html", username = username)
    else:
        return render_template("signup.html", un_error = un_error, pw_error = pw_error, vpw_error = vpw_error, 
        email_error = email_error, username = username, email = email)

app.route("/")
def index():
    return render_template(signup.html)

app.run()