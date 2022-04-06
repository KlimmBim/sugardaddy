from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World, this is a test!</p>"
#Test, das geht nicht
