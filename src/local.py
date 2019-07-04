import os
from flask import Flask, render_template, request

__author__ = '0xprateek'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
    return '',204

if __name__ == "__main__":

    try:
        import sys,argparse
        parser = argparse.ArgumentParser()
    except:
        print("Moudle not found")

    parser.add_argument('-port',help="Port address",default = 5050)

    args = parser.parse_args()
    app.run(port=args.port, debug=True)
