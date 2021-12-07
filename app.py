from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Disney')
def disney_page():
    return render_template("Disney.html")


@app.route('/Hulu')
def hulu_page():
    return render_template("Hulu.html")


@app.route('/Netflix')
def netflix_page():
    return render_template("Netflix.html")


@app.route('/Prime')
def prime_page():
    return render_template("Prime.html")


if __name__ == '__main__':
    app.run()
