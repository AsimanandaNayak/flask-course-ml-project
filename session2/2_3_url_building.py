from flask import Flask,redirect,url_for
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Welcome to our Page</h1>"


@app.route("/pass/<sname>/<int:marks>")
def passed(sname,marks):
    return f"<h1>Congratz {sname} ... You are pass for scoring {marks}</h1>"

@app.route("/fail/<sname>/<int:marks>")
def failed(sname,marks):
    return f"<h1>OOPs {sname}....You'he fail for {marks} score </h1>"

@app.route("/score/<name>/<int:mark>")
def score(name,mark):
    if(mark <= 30):
        # Redirect towards Fail webpage
        return redirect(url_for("failed",sname=name,marks=mark))
    else:
        # Redirect towards Pass webpage
        return redirect(url_for("passed",sname=name,marks=mark))



if __name__ == "__main__":
    app.run(debug=True)