from flask import Flask, request,redirect
from flask import render_template
import sqlite3
from servicio import*

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes')
def index_clientes():
    
    conexion=Servicio.conectar()
    conexion.row_factory = sqlite3.Row
    clientes=Servicio.consultar(conexion)
    conexion.close()
    return render_template('/modules/clientes/index.html',clientes=clientes)
   
@app.route('/clientes/create')
def create():
    return render_template('/modules/clientes/create.html')

@app.route('/clientes/create/guardar',methods=['POST'])
def clientes_guardar():
    nombre=request.form['nombre']
    apellido=request.form['apellido']
    email=request.form['email']
    conexion=Servicio.conectar()
    datos=Servicio.crear(nombre,apellido,email,conexion)
    return redirect('/clientes')

@app.route('/clientes/editar/<int:id>')
def clientes_editar(id):
    conexion=Servicio.conectar()
    conexion.row_factory = sqlite3.Row
    clientes=Servicio.buscar(id,conexion)
    conexion.close()
    return render_template('/modules/clientes/edit.html',clientes=clientes)

@app.route('/clientes/editar/actualizar',methods=['POST'])
def clientes_actualizar():
    id=request.form['id']
    nombre=request.form['nombre']
    apellido=request.form['apellido']
    email=request.form['email']
    conexion=Servicio.conectar()
    Servicio.actualizar(nombre,apellido,email,id,conexion)
    return redirect('/clientes')
    
@app.route('/clientes/borrar/<int:id>')
def clientes_borrar(id):
    conexion=Servicio.conectar()
    conexion.row_factory = sqlite3.Row
    eliminar=Servicio.borrar(id,conexion)
    return redirect('/clientes')

if __name__=='__main__':
    app.run(debug=True)
    