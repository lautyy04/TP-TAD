
#una cola para el alta de los clientes del ultimo mes
def crearCola():
    #Crea una cola vacia
    cola=[]
    return cola

def esVacia(cola):
    #Retorna Verdadero si la cola no tiene elementos
    return len(cola)==0

def encolar(cola,elem):
    #Agrega un elemento al final de la cola
    cola.append(elem)
    
def desencolar(cola):
    #Retorna y elimina el primer elemento de la cola
    elem= cola.pop(0)    
    return elem

def tamanioCola (cola):
    #Retorna la cantidad de elementos de la cola
    return len(cola)

def copiarCola(cola1,cola2):
   aux=crearCola()              #crea una cola auxiliar (momentanea)
   while not esVacia(cola2):    # mientras no esta está vacia, desencolar
        elem=desencolar(cola2)
        encolar(aux,elem)       #encolar en auxiliar
   while not esVacia(aux):      #si auxiliar no está vacio, desencolar 
        elem=desencolar(aux)    
        encolar(cola1,elem)     #volvemos a completar cola1
        encolar(cola2,elem)     #completamos cola2
        
