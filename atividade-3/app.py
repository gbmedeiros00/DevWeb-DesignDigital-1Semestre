from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'atividade3'
mysql = MySQL(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route('/add_task', methods=['POST'])
def add_task():
    if request.method == 'POST':
        cont_email = request.form['cont_email']
        cont_msg = request.form['cont_msg']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contato (cont_email, cont_msg) VALUES (%s, %s)", (cont_email, cont_msg))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('contato'))
    
@app.route("/requisicoes")
def requisicoes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM contato")
    contato = cur.fetchall()
    cur.close()
    return render_template('requisicoes-contato.html', contato=contato)

@app.route("/quemsomos")
def quemsomos():
    return render_template('quemsomos.html')

if __name__ == '__main__':
    app.run(debug=True)