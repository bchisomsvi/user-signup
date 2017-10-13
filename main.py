from flask import Flask, request, render_template
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=["POST"])
def user_validation():
    username = request.form['username']
    password = request.form['password']
    verify_pw = request.form['verifypassword']
    email = request.form['email']
    template = jinja_env.get_template("index.html")

    un_error = ""
    pw_error = ""
    vpw_error = ""
    email_error = ""

    if username == "" or " " in username or len(username) < 3 or len(username) > 20:
        un_error = "Not a valid Username"
    if password == "" or " " in password or len(password) < 3 or len(username) > 20:
        pw_error = "Invalid Password"
    if verify_pw == "" or verify_pw != password:
        vpw_error = "Passwords do not match"
    if email != "":
        if "@" not in email or "." not in email or " " in email or len(email) < 3 or len(email) > 20:
            email_error = "Invalid Email"
    if not email_error and not un_error and not pw_error and not vpw_error:
        return render_template("welcome.html", username = username)
    else:
        return render_template('index.html', un_error = un_error, pw_error = pw_error, vpw_error = vpw_error, email_error = email_error)

@app.route("/")
def index():
    template = jinja_env.get_template('index.html')
    return template.render()
app.run()