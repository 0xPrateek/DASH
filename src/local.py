import sys

try:
    import os
    from flask import Flask, render_template, request
except:
    print("Module not found\n    Make sure you have installed 'requirements.txt' and configured DASH")
    sys.exit(0)

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
        import argparse
        parser = argparse.ArgumentParser()
    except:
        print("Module not found\n    Make sure you have installed 'requirements.txt' and configured DASH")
        sys.exit(0)

    parser.add_argument('-port',help="Port address")
    parser.add_argument('-path',help="Path address")

    args = parser.parse_args()

    app.run(port=args.port, debug=True)
