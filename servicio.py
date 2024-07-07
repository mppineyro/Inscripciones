#CONTROLADOR

import sqlite3
from consultas import*
from clientes import*

class Servicio:
    
    def conectar():
        miConexion=sqlite3.connect("datatable.db")
        return miConexion
    
    #CREAR TABLE
    def conexionBBDD(miConexion):
        miCursor=miConexion.cursor()
        miCursor.execute(Consulta.CREATE)
    
    #DELETE TABLE
    def eliminarBBDD(miConexion):
        miCursor=miConexion.cursor()
        miCursor.execute(Consulta.DELETE)
    
    #READ 
    def consultar(miConexion):
        miCursor=miConexion.cursor()
        miCursor.execute(Consulta.SELECT)
        return miCursor.fetchall()
    
    #CREATE
    def crear(nombre,apellido,email,miConexion):
        miCursor=miConexion.cursor()
        cliente=Cliente(nombre,apellido,email)
        miCursor.execute(Consulta.INSERT,(cliente.info()))
        miConexion.commit()
        
    #UPDATE
    def actualizar(nombre,apellido,email,id,miConexion):
        miCursor=miConexion.cursor()
        cliente=Cliente(nombre,apellido,email)
        info=list(cliente.info())
        info.append(id)
        tuple(info)
        miCursor.execute(Consulta.UPDATE,info)
        miConexion.commit()
        
    #DELETE
    def borrar(id,miConexion):
        miCursor=miConexion.cursor()
        miCursor.execute(Consulta.DELETE,(id,))
        miConexion.commit() 
     
    #BUSCAR   
    def buscar(id,miConexion):
        miCursor = miConexion.cursor()
        miCursor.execute(Consulta.SEARCH,(id,))
        return  miCursor.fetchone()