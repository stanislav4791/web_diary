from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'diary'
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


# @app.route("/diary/create", methods=['GET','POST'])
# def create():
#     if request.method == ['POST']:
#         save_entry(request.form)
#     elif request.method == ['GET']:
#         return render_template("create.html", title='CREATE')
        

if __name__ == "__main__":
    app.run(debug=True)

# if request.method == ['GET']:
    #     return render_template("create.html", title='HOME')
    # elif request.method == ['POST']:
    #     save_entry(request.form)
    #     return render_template("index.html", title='HOME')

    # def save_entry(form):

#     if request.method == "POST":
#         date = form['name']
#         heading = form['heading']
#         content = form['content']

#         cur = mysql.connection.cursor()
#         cur.execute('INSERT INTO diary (date, heading, content) VALUES (%s, %s, %s)', (date, heading, content))
#         mysql.connection.commit()
#         return redirect("/")