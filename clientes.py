#MODELO

'''Creación de los datos de cada cliente, sin incorporar el id'''
class Cliente:
    #Creación del constructor
    def __init__(self, nombre, apellido, email) -> None:
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        
    def info(self):
        return self.nombre,self.apellido,self.email