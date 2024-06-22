from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)
 
@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
      
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute('''SELECT * FROM inscriptos''')
        results = cursor.fetchall()
        cursor.close()
        return render_template('login.html', results=results)

    
   
    if request.method == 'POST':
      action = request.form['action']
    
      if action == 'insert':
        name = request.form['name']
        mail = request.form['mail']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO inscriptos VALUES(%s,%s,%s)''',(None,name,mail))
        mysql.connection.commit()
        cursor.close()
        return f"Inscripto '{name}' insertado correctamente"
    
      elif action == 'delete':
        inscripto_id = request.form.get('inscripto_id')
        if inscripto_id:
            cursor = mysql.connection.cursor()
            cursor.execute('''DELETE FROM inscriptos WHERE inscripto_id = %s''', (inscripto_id,))
            mysql.connection.commit()
            cursor.close()
            return f"Inscripto con ID {inscripto_id} eliminado correctamente"
 
app.run(host='localhost', port=5000)