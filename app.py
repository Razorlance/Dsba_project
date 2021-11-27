from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    print(min(map(int, input().split()), key=lambda x: (not (x % 2), x)))
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
