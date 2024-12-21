from flask import Flask, redirect, url_for,render_template
from employees import employee_data

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title = "Home")

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/pass/<sname>/<int:marks>")
def passed(sname, marks):
    return f"<h1>Congratulations {sname}! You passed with a score of {marks}!</h1>"

@app.route("/fail/<sname>/<int:marks>")
def failed(sname, marks):
    return f"<h1>Sorry {sname}, you scored {marks} and failed.</h1>"

@app.route("/score/<name>/<int:mark>")
def score(name, mark):
    if mark < 30:
        return redirect(url_for("failed", sname=name, marks=mark))
    else:
        return redirect(url_for("passed", sname=name, marks=mark))

@app.route("/employees")
def employees():
    return render_template("employees.html",title = "Employees",emps=employee_data)

@app.route("/employees/managers")
def manager():
    return render_template("managers.html",title = "Manager",emps = employee_data)

@app.route("/guess_game")
def guess_game():
    return render_template("guess_game.html",title = "Guess Game")


if __name__ == "__main__":
    app.run(debug=True)
