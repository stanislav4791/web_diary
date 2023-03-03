from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'diary'

mysql = MySQL(app)

def save_entry():

    if request.method == "POST":
        date = request.form['name']
        heading = request.form['heading']
        content = request.form['content']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO diary (date, heading, content) VALUES (%s, %s, %s)', (date, heading, content))
        mysql.connection.commit()



