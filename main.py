from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQLdb
from db import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title='HOME')


@app.route("/diary", methods = ['POST'])
def insert():
    return insert_blog()

if __name__ == "__main__":
    app.run()