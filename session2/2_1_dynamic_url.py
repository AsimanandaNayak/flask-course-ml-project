from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hey Everyone it is home page </h1>"


@app.route("/welcome/steve")
def welcome_steve():
    return "<h1>Wlcome Steve</h1>"

@app.route("/welcome/Tony")
def welcome_tony():
    return "<h1>Welcome Tony</h1>"


#Create dynamically for any name 
@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1> Welcome {name.title()}"


if __name__ == "__main__":
    app.run(debug=True)