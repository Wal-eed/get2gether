from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "test.exe"


if __name__ == _'__main__':
    app.run()