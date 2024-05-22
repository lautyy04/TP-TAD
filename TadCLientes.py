#donde tendremos todos los clientes 
#tad compuesto

def crearClientes():
    #crear registro de clientes
    clientes=[]
    return clientes 

def agregarClientes(clientes,client):
    #agrega un cliente al sistema 
    clientes.append(client)

def eliminarClientes(clientes,client):
    #eliminar clientes del sistema
    clientes.remove(client)

def recuperarClientes(clientes,i):
    #retorna el cliente de la posición asignada    
    return clientes[i]

def tamanio(clientes):
    #retorna la cantidad de clientes en el sistema
    return len(clientes)