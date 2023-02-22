from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'sql7.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql7598384'
app.config['MYSQL_PASSWORD'] = 'q4qIaKsMQW'
app.config['MYSQL_DB'] = 'sql7598384'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html", title='HOME')

 
@app.route("/diary")
def diary():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM entries")
    data = cur.fetchall()
    cur.close()
    return render_template("index.html", data = data, title='HOME')


@app.route("/diary/create", methods=['GET','POST'])
def insert():
    print("PRINT")
    if request.method == 'GET':
        print("Menee getiin")
        return render_template("create.html", title="CREATE")
    elif request.method == 'POST':
        print("Menee postiin")
        date = request.form['date']
        heading = request.form['heading']
        content = request.form['content']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO entries (date, heading, content) VALUES (%s, %s, %s)", (date, heading, content))
        mysql.connection.commit()
        return redirect(url_for('diary'))

    
    
        
if __name__ == "__main__":
    app.run(debug=True)