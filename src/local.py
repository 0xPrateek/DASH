import os
from flask import Flask, render_template, request

__author__ = '0xprateek'

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=['POST'])
def upload():

    target = os.path.join(args.path)
    print(target)

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

    parser.add_argument('-port',help="Port address")
    parser.add_argument('-path',help="Path address")

    args = parser.parse_args()

    app.run(port=args.port, debug=True)
