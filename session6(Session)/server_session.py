from flask import Flask,redirect,url_for,render_template,flash,session ,request
#Here session is a Dictionary for storing details
from forms import LoginForm
from flask_session import Session


app = Flask(__name__)

app.config["SECRET_KEY"] = "secret_key"
app.config["SESSION_TYPE"] = "filesystem"

Session(app) #It says it is a server session


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html",title="Home")

@app.route("/about")
def about():
    if "user_name" not in session: #Is open username is already Loged in or not
        flash("Login Requiered!!")
        return redirect(url_for("login" , next=request.url))
    else:
        flash(f"Hii {session["user_name"]}, Have a good day !")
    return render_template("about.html",title="About")

@app.route("/contact")
def contact():
    if "user_name" not in session:
        flash("Login Required!!")
        return redirect(url_for("login",next=request.url))
    else:
        flash(f"Hii {session["user_name"]},Have a good Day !")
    return render_template("contact.html",title="Contact")

@app.route("/login", methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['user_name'] = form.username.data
        flash(f"Successfully logged in as {session["user_name"].title()} !")
        next_url = request.args.get("next") # it get the page where the flow comes from which is stored in "next" 
        #If it comes from direct Home page the "next" contains null
        return redirect(next_url or url_for("home")) #it next_url contain it will direct go to Home page
    
    return render_template("login.html",title="Login",form = form)

if __name__ == "__main__":
    app.run(debug=True)
