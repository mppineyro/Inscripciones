from flask import Flask,render_template, request, redirect
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)
 
@app.route('/')
def ini():
    return redirect('/login')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute('''SELECT * FROM inscriptos''')
        results = cursor.fetchall()
        cursor.close()
        return render_template('login.html', results=results)
      
@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        mail = request.form['mail']
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO inscriptos VALUES(%s,%s,%s)''', (None, name, mail))
        mysql.connection.commit()
        cursor.close()
        return redirect('/login')
      
    return render_template('alta.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        inscripto_id = request.form['inscripto_id']
        if inscripto_id:
            cursor = mysql.connection.cursor()
            cursor.execute('''DELETE FROM inscriptos WHERE inscripto_id = %s''', (inscripto_id,))
            mysql.connection.commit()
            cursor.close()
            return redirect('/login')
    
    return render_template('baja.html')

@app.route('/modificar', methods=['GET', 'POST'])
def modificar():
    if request.method == 'POST':
        inscripto_id = request.form.get('inscripto_id')
        name = request.form.get('name')
        mail = request.form.get('mail')
        
        if inscripto_id and name and mail:
            cursor = mysql.connection.cursor()
            cursor.execute('''UPDATE inscriptos SET name = %s, mail = %s WHERE inscripto_id = %s''', (name, mail, inscripto_id))
            mysql.connection.commit()
            cursor.close()
            return redirect('/login')
    
    return render_template('modificar.html')

app.run(host='localhost', port=5000)