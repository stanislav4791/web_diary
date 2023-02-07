from flask import request, redirect
from main import app
from flask_mysqldb import MySQL


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'diary'

mysql = MySQL(app)

def insert_blog():

    if request.method == "POST":
        date = request.form['name']
        heading = request.form['heading']
        content = request.form['content']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO diary (date, heading, content) VALUES (%s, %s, %s)', (date, heading, content))
        mysql.connection.commit()
        return redirect("/")

