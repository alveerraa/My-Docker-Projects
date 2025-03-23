from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is a persistent volume test!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

