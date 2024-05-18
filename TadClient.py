#creamos TAD para cada cliente
from datetime import datetime

client=[0,0,"","","",0,0]


def crearClient():
    #crea un cliente vacio
    client=[0,0,"","","",0,0]
    return client

def cargarClient(client,nro,dni,ape,nom,fech,tip,prec):
    #carga los datos de los clientes
    
    client[0]=nro       #numero de cliente
    client[1]=dni       #DNI de cliente
    client[2]=ape       #apellido de cliente
    client[3]=nom       #nombre de cliente
    client[4]=fech      #fecha de alta
    client[5]=tip       #tipo de servicio
    client[6]=prec      #precio del servicio contratado

#retornos

def verNumero(client):
    #retorna el nombre del cliente
    return client[0]

def verDni(client):
    #retorna DNI del cliente
    return client[1]

def verApellido(client):
    #retorna el apellido del cliente
    return client[2]

def verNombre(client):
    #retorna nombre del cliente 
    return client[3]

def verFecha(client):
    #retorna fecha de alta del cliente
    return client[4]

def verTipo(client):
    #retorna tipo de servicio del cliente
    return client[5]

def verPrecio(client):
    #retorna precio del servicio contratado
    return client[6]

#modificar

def modNom(client,nom):
    #modificar el nombre del cliente
    client[3]=nom

def modNro(client,nro):
    #modifica el numero del cliente
    client[0]=nro    

def modDni(client,dni):
    #modificar el dni del cliente
    client[1]=dni

def modApe(client,ape):
    #modifica el apellido del cliente
    client[2]=ape

def modFech(client,fech):
    #modifica la fecha de alta 
    client[4]=fech

def modTip(client,tip):
    #modificar tipo de servicio
    client[5]=tip

def modPre(client,prec):
    #modificar precio del servicio
    client[6]=prec    


    