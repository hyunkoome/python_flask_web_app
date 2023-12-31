from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flask, Hyunkoo"

@app.route("/hello/<name>", methods=["GET", "POST"], endpoint="hello-endpoint")
def hello(name):
    # return f"Hello, {name}"
    return "Hello, {}".format(name)

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)

with app.test_request_context():
    # /
    print(url_for("index"))

    # /hello/world
    print(url_for("hello-endpoint", name="world"))

    # /name/Hyunkoo?page=1
    print(url_for("show_name", name="Hyunkoo", page="1"))
