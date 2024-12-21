
from flask import Flask , render_template , url_for , flash
from werkzeug.utils import redirect

from forms import SignupPage , LoginPage

app = Flask(__name__)
app.config["SECRET_KEY"] = "this_is_a_secret_key"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title = "Home")

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/login" , methods=["GET","POST"])
def login():
    form = LoginPage()
    email = form.email.data
    pw = form.password.data
    if form.validate_on_submit():
        if email == "a@b.com" and pw == "12345" :
            flash(f"Successfully Logedin ")
            return redirect(url_for("home"))
    return render_template("login.html",title = "Login",form = form)

@app.route("/signup",methods=["GET","POST"])
def signup():
    form = SignupPage()
    if form.validate_on_submit():
        flash(f"Successfully Registerd {form.username.data}")
        return redirect((url_for("home")))
    return render_template("signup.html",title = "Signup" , form = form)


if __name__ == "__main__":
    app.run(debug=True)