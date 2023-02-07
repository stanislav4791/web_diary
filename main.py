from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", title='HOME')


if __name__ == "__main__":
    app.run()