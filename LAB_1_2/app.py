#Source: https://pythonspot.com/flask-hello-world/
from flask import Flask
app = Flask(__name__)
import sys

@app.route("/")
def hello():
    #as per: https://stackoverflow.com/questions/44405708/flask-doesnt-print-to-console
    print("Użytkownik odwiedził stronę główną.", flush=True)
    return "<h1>Hello World!</h1>"


if __name__ == "__main__":
    app.run()