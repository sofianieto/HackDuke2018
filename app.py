from flask import Flask
import requests
import random
from PIL import Image

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()