from flask import Flask , redirect , url_for
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Welcome to our Page</h1>"

@app.route("/pass")
def passed():
    return "<h1>Congratz, You are Pass !!</h1>"

@app.route("/fail")
def failed():
    return "<h1>OOPs...You are Failed"

@app.route("/score/<name>/<int:mark>")
def score(name,mark):
    if mark<30:
        #redirected towords Failed webpagw
        return redirect(url_for("failed")) #it will run failed function
    else:
        #redirected towards Passed Webpage
        return redirect(url_for("passed")) #it will run passed function



if __name__ == "__main__":
    app.run(debug=True)