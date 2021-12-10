from flask import Flask, render_template
from static.Calculations.calculations import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", data=overall_data)


@app.route('/Disney')
def disney_page():
    return render_template("Disney.html", data=disney_data)


@app.route('/Hulu')
def hulu_page():
    return render_template("Hulu.html", data=hulu_data)


@app.route('/Netflix')
def netflix_page():
    return render_template("Netflix.html", data=netflix_data)


@app.route('/Prime')
def prime_page():
    return render_template("Prime.html", data=prime_data)


if __name__ == '__main__':
    app.run()
