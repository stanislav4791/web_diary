from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import bcrypt

app = Flask(__name__)


app.secret_key = 'stanistheman'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'diary'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/register', methods =['GET', 'POST'])
def register():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password'].encode("utf-8")
        email = request.form['email']
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO user VALUES (%s, %s, %s, %s)', ('', username, hashed, email))
        mysql.connection.commit()
        flash("Successful registration")
        return redirect(url_for('login'))
    elif request.method == 'GET':
        return render_template("register.html", title='REGISTER')

@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password'].encode("utf-8")
        print(password)
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM user WHERE username = %s', [username])
        user = cur.fetchone()
        res = list(user.items())
        stored = res[2][1].encode("utf-8")
        print(stored)
        if user and bcrypt.checkpw(password, stored):
            session['loggedin'] = True
            session['user_id'] = user['user_id']
            session['username'] = user['username']
            session['email'] = user['email']
            flash("You are logged in")
            return render_template('index.html')
        else:
            flash("Check you credentials")
            return redirect("/login")
    elif request.method == 'GET':
        return render_template('login.html', title='LOGIN')


@app.route("/")
def index():
    return render_template("index.html", title='HOME')

 
@app.route("/diary")
def diary():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM entries")
    data = cur.fetchall()
    cur.close()
    if data:
        return render_template("diary.html", data = data, title='HOME')
    else:
        flash("No diary entries")
        return render_template("diary.html", data = data, title='HOME')

@app.route("/diary/create", methods=['GET','POST'])
def insert():
    if request.method == 'GET':
        return render_template("create.html", title="CREATE")
    elif request.method == 'POST':
        user_id = session['user_id']
        date = request.form['date']
        heading = request.form['heading']
        content = request.form['content']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO entries (user_id, date, heading, content) VALUES (%s, %s, %s, %s)", (user_id, date, heading, content))
        mysql.connection.commit()
        flash("Entry created")
        return redirect(url_for('diary'))

@app.route("/diary/<id>")
def show_entry(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, date, heading, content FROM entries WHERE id =%s", [id])
    entry = cur.fetchone()
    return render_template("partials/entry.html", entry = entry, title="ENTRY")

@app.route("/diary/update/<id>", methods=['GET','POST'])
def update(id):
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, date, heading, content FROM entries WHERE id =%s", [id])
        data = cur.fetchone()
        return render_template("update.html", data = data, title="UPDATE")
    elif request.method == 'POST':        
        date = request.form['date']
        heading = request.form['heading']
        content = request.form['content']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE entries set date='%s', heading='%s', content='%s' WHERE id='%s' " % (date, heading, content, id))
        mysql.connection.commit()
        flash("Entry updated")
        return redirect(url_for('diary'))


@app.route("/diary/delete/<id>", methods=['GET', 'POST'])

def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM entries WHERE id = %s", [id])
    mysql.connection.commit()
    flash("Entry deleted")
    return redirect(url_for('diary'))



    





if __name__ == "__main__":
    app.run(debug=True)