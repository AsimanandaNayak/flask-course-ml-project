from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1> Hey Everyone it is home page </h1>"


@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1> Hey {name} welcome to our page"



@app.route("/addition/<num>")
def addition(num):
    return f"<h1>the number is {num} and addition is {int(num) + 10}</h1>"



@app.route("/addition1/<int:num>")
def addition1(num):
    return f"<h1> the number is {num} and addition is {num + 10}"


@app.route("/addition_two/<int:num1>/<int:num2>")
def addition_two(num1,num2):
    return f"<h1> {num1} + {num2} is {num1 + num2}</h1>"





@app.route("/about")
def about():
    return "<h1> Hey  Evveryone it is about page. </h1>"


if __name__ == "__main__":
    app.run(debug=True)