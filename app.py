import os
import sys

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    print("Hello endpoint called!")
    return "Hello from Python App"

@app.route("/dummy")
def dummy():
    print("Dummy endpoint called!")
    dummy_appsetting = os.environ.get("DUMMY_APPSETTING")
    if dummy_appsetting is not None:
        return dummy_appsetting
    return "Appsetting not found!"

@app.route("/placeholder")
def placeholder():
    print("Placeholder endpoint called!")
    return "97a876af-2468-47ba-a7b2-714d119e6823"