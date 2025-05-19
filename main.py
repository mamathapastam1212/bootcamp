# print("__name__ =", __name__)
# print("__file__=", __file__)

from flask import Flask
import os
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello world"

if __name__ == "__main__":
    app.run(host="0.0.0.0")