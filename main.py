import sqlite3
from flask import Flask, render_template, request
from flask import g

DATABASE = 'db.sqlite3'
app = Flask(__name__)



@app.route ('/', methods=['GET', 'POST'])
def list():
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from hymns_textblock where parent_block_id IS NULL or parent_block_id = 0")
    rows = cur.fetchall()
    return render_template("home.html",rows = rows)

@app.route ('/view/<num>', methods=['GET', 'POST'])
def view(num):
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    sqlcom = "select * from hymns_textblock where parent_block_id = " + str(num)
    cur.execute(sqlcom)
    rows = cur.fetchall()

    if rows:
        return render_template("view.html",rows = rows) #,q = sqlcom

    if not rows:
        sqlcom = "select * from hymns_paragraph where parent_block_id = " + str(num)
        cur.execute(sqlcom)
        pars = cur.fetchall()
        return render_template("view.html",pars = pars)


if __name__ == "__main__":
    app.run(debug=True)
    list()
