from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flask, Hyunkoo"

@app.route("/hello/<name>", methods=["GET", "POST"], endpoint="hello-endpoint")
def hello(name):
    # return f"Hello, {name}"
    return "Hello, {}".format(name)

