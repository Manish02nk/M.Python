from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<b> manish lobes python</b>'


if __name__ == "__main__":
    app.run(debug=True)
