from datetime import datetime
from TadClient import *
from TadCLientes import *
from tadCola import *
from random import randint,choice

def limpiarPantalla():
    """limpia la pantalla """
    from os import name as sys_name, system

    if (sys_name == 'LINUX') or (sys_name == 'posix'): system('clear')# para linux
    else: system('cls')# para windows

cantidadClientes=50 #variable que dice cuantos clients aleatorios se van a generar 

#funcion para generacion aleatoria de datos
def generacionClientes(clientes,n:int):
    #lista de numeros de clientes
    listadoNumeros=[(randint(2222,4444)) for _ in range (n)] 

    #lista de dni de clientes aleatorios
    listadoDni=[(randint(20000000,40000000)) for _ in range (n)]
    
    #lista de apellidos aleatorios (para pruebas)
    listadoApelldo=[(choice(["Gómez", "Martínez", "Rodríguez", "López", "Pérez", "García", "Fernández", "Díaz", "Moreno", "Muñoz",
    "Álvarez", "Romero", "Sánchez", "González", "Torres", "Ortega", "Ruiz", "Jiménez", "Dominguez", "Vázquez",
    "Ramos", "Serrano", "Blanco", "Núñez", "Navarro", "Molina", "Delgado", "Suárez", "Ortiz", "Castro",
    "Rubio", "Márquez", "Santos", "Herrera", "Vega", "Flores", "Cabrera", "Reyes", "Calderón", "Ramírez",
    "Morales", "Santiago", "Gutiérrez", "Aguilar", "Giménez", "Peralta", "Medina", "Vidal", "Iglesias",
    "Fuentes", "Cruz", "Arias", "Vargas", "Campos", "Carmona", "Lozano", "Cortés", "Pastor", "Aguirre",
    "Guerrero", "Valero", "Sanchez", "Montero", "Navarro", "Vicente", "Lorenzo", "Marín", "Guerrero",
    "Barrios", "Carretero", "Rojas", "Olivares", "Soto", "Méndez", "Lara", "Salazar", "Solís", "Peña",
    "Pizarro", "Ferrer", "Estévez", "Aguayo", "Arenas", "Bermúdez", "Cordero", "Casado", "Montes", "Gallego",
    "Hernández", "Díez", "Valle", "Herrero", "Bellido", "Fernando", "Luna", "Cano", "Guillén", "Carvajal"])) for _ in range (n)]
    
    #lista de nombres aleatorios (para pruebas)
    listadoNombres=[(choice(["Juan", "María", "Pedro", "Luisa", "Ana", "Carlos", "Laura", "Miguel", "Alejandro", "Lucía",
    "Sofía", "Diego", "Valentina", "Pablo", "Camila", "Javier", "Paula", "Daniel", "Gabriela", "Andrés",
    "Natalia", "Felipe", "Carolina", "Fernando", "Isabella", "David", "Sara", "José", "Valeria", "Manuel",
    "Tatiana", "Jorge", "Elena", "Francisco", "Clara", "Ricardo", "Daniela", "Martín", "Verónica", "Esteban",
    "Juliana", "Roberto", "Adriana", "Gustavo", "Cristina", "Emilio", "Catalina", "Sebastián", "Patricia",
    "Antonio", "Mónica", "Alberto", "Marcela", "Rafael", "Vanessa", "Mario", "Alejandra", "Carlos", "María",
    "Mauricio", "Jessica", "Ángel", "Paola", "Jesús", "Cindy", "Simón", "Carla", "Leonardo", "Melissa",
    "Héctor", "Lorena", "Raúl", "Sandra", "Santiago", "Natalie", "Fabián", "Yolanda", "Kevin", "Brenda",
    "Eduardo", "Isabel", "Luis", "Ingrid", "Andrea", "Julián", "Gloria", "Oscar", "Luciana", "Jaime", "Diana",
    "Iván", "Rosa", "Armando", "Rocio", "Juan Pablo", "Liliana", "Diego Alejandro", "Marisol", "Fernando José"]))for _ in range (n)]

    #listado de fechas              #AÑO        MES             DIA
    listadoFechas=[datetime(randint(2018,2024),randint(1,12),randint(1,28))for _ in range(n)]   #genera fechas entre ese rango de años ,meses ,dias 

    listadoTipo=[(choice(["MEDIA","BASICO","PREMIUM"]))for _ in range(n)]   

    listadoPrecios=[(randint(1000, 2000)) for _ in range(n)]         #genera precios entre ese rango 1000 a 2000                           

    
    for nro,dni,ape,nom,fech,tip,prec in zip(listadoNumeros,listadoDni,listadoApelldo,listadoNombres,listadoFechas,listadoTipo,listadoPrecios): #guarda los datos en orden segun estes separados por la ,
        nuevoCliente=crearClient()  #declaramos la funcino
        cargarClient(nuevoCliente,nro,dni,ape,nom,fech,tip,prec)    #cargamos el cliente
        agregarClientes(clientes,nuevoCliente)                      #agregamos el cliente


#generamos una cola de clientes para trabajarla en la opcion 8 (no afecta a las listas de clientes)
def generacionColaClientes(cola,n:int):
    #lista de numeros de clientes
    listadoNumeros=[(randint(2222,4444)) for _ in range (n)] 

    #lista de dni de clientes aleatorios
    listadoDni=[(randint(20000000,40000000)) for _ in range (n)]

    listadoApelldo=[(choice(["Gómez", "Martínez", "Rodríguez", "López", "Pérez", "García", "Fernández", "Díaz", "Moreno", "Muñoz",
    "Álvarez", "Romero", "Sánchez", "González", "Torres", "Ortega", "Ruiz", "Jiménez", "Dominguez", "Vázquez",
    "Ramos", "Serrano", "Blanco", "Núñez", "Navarro", "Molina", "Delgado", "Suárez", "Ortiz", "Castro",
    "Rubio", "Márquez", "Santos", "Herrera", "Vega", "Flores", "Cabrera", "Reyes", "Calderón", "Ramírez",
    "Morales", "Santiago", "Gutiérrez", "Aguilar", "Giménez", "Peralta", "Medina", "Vidal", "Iglesias",
    "Fuentes", "Cruz", "Arias", "Vargas", "Campos", "Carmona", "Lozano", "Cortés", "Pastor", "Aguirre",
    "Guerrero", "Valero", "Sanchez", "Montero", "Navarro", "Vicente", "Lorenzo", "Marín", "Guerrero",
    "Barrios", "Carretero", "Rojas", "Olivares", "Soto", "Méndez", "Lara", "Salazar", "Solís", "Peña",
    "Pizarro", "Ferrer", "Estévez", "Aguayo", "Arenas", "Bermúdez", "Cordero", "Casado", "Montes", "Gallego",
    "Hernández", "Díez", "Valle", "Herrero", "Bellido", "Fernando", "Luna", "Cano", "Guillén", "Carvajal"])) for _ in range (n)]

    listadoNombres=[(choice(["Juan", "María", "Pedro", "Luisa", "Ana", "Carlos", "Laura", "Miguel", "Alejandro", "Lucía",
    "Sofía", "Diego", "Valentina", "Pablo", "Camila", "Javier", "Paula", "Daniel", "Gabriela", "Andrés",
    "Natalia", "Felipe", "Carolina", "Fernando", "Isabella", "David", "Sara", "José", "Valeria", "Manuel",
    "Tatiana", "Jorge", "Elena", "Francisco", "Clara", "Ricardo", "Daniela", "Martín", "Verónica", "Esteban",
    "Juliana", "Roberto", "Adriana", "Gustavo", "Cristina", "Emilio", "Catalina", "Sebastián", "Patricia",
    "Antonio", "Mónica", "Alberto", "Marcela", "Rafael", "Vanessa", "Mario", "Alejandra", "Carlos", "María",
    "Mauricio", "Jessica", "Ángel", "Paola", "Jesús", "Cindy", "Simón", "Carla", "Leonardo", "Melissa",
    "Héctor", "Lorena", "Raúl", "Sandra", "Santiago", "Natalie", "Fabián", "Yolanda", "Kevin", "Brenda",
    "Eduardo", "Isabel", "Luis", "Ingrid", "Andrea", "Julián", "Gloria", "Oscar", "Luciana", "Jaime", "Diana",
    "Iván", "Rosa", "Armando", "Rocio", "Juan Pablo", "Liliana", "Diego Alejandro", "Marisol", "Fernando José"]))for _ in range (n)]

    #TENER EN CUENTA QUE SOLO ES EL ULTIMO MES ( SOLO TOMA EL AÑO 2024)
    listadoFechas=[datetime(randint(2022,2024),randint(1,12),randint(1,28))for _ in range(n)]   #genera fechas entre ese rango de años ,meses ,dias 

    listadoTipo=[(choice(["MEDIA","BASICO","PREMIUM"]))for _ in range(n)]   

    listadoPrecios=[(randint(1000, 2000)) for _ in range(n)]         #genera precios entre ese rango 1000 a 2000                           

    
    for nro,dni,ape,nom,fech,tip,prec in zip(listadoNumeros,listadoDni,listadoApelldo,listadoNombres,listadoFechas,listadoTipo,listadoPrecios): #guarda los datos en orden segun estes separados por la ,
        nuevoCliente=crearClient()  #declaramos la funcion
        cargarClient(nuevoCliente,nro,dni,ape,nom,fech,tip,prec)    #cargamos el cliente
        encolar(cola,nuevoCliente)                     


def imprimirMenu(): #funcion de menu
    print(f"-------------------- {tamanio(clientes)} CLIENTES ACTUALES ----------------")
    print("¿que desea realizar?")   
    print("agregar cliente                         ------> 1 ")  
    print("modificar cliente                       ------> 2 ")
    print("eliminar cliente                        ------> 3 ")                      
    print("listado de todos los clientes           ------> 4 ")  
    print("eliminar cliente por servicio           ------> 5 ")  
    print("aplicar descuentos a clientes antiguos  ------> 6 ")  
    print("clientes con promociones vigentes       ------> 7 ")  
    print("altas de clientes del ultimo mes        ------> 8 ")

def imprimirCliente(client,tabulados:int=1):    #muestra como es cada cliente
    tabulaciones='\t'*(tabulados)
    textoImprimir=f"""
    {tabulaciones} numero de cliente: {verNumero(client)}
    {tabulaciones} dni de cliente: {verDni(client)}
    {tabulaciones} apellido de cliente: {verApellido(client)}
    {tabulaciones} nombre de cliente: {verNombre(client)}
    {tabulaciones} fechas de alta: {verFecha(client)}
    {tabulaciones} tipo de servicio: {verTipo(client)}
    {tabulaciones} precio de servicio: {verPrecio(client)}"""

    print(textoImprimir)


#FUNCIONES Y RESOLUCION DE ACTIVIDADES

#FUNCION DE AGREGAR CLIENTE
def opcion1(clientes):          
    try:
        nro=int(input("ingrese el numero de cliente"))  
        dni=int(input("ingrese el dni del cliente"))
        ape=input("ingrese apellido")
        nom=input("ingrese nombre")
        fech=datetime.strptime(input("ingrese la fecha en el siguiente formato dd/mm/yyyy"), "%d/%m/%Y")            #se debe respetar el formato
        tip=["BASICO","MEDIA","PREMIUM"][int(input("ingrese el tipo de servicio 1=BASICO, 2=MEDIA, 3=PREMIUM "))-1]     #la primer lista es para que cuando un usuario ingrese un numero, se guarde como BASICO,MEDIO,PREMIUM y no como numeros
        prec=float(input("ingrese precio del servicio"))
        
    except:
        print("datos mal pasados")                           
    
    nuevoCliente=crearClient()                                  #declaramos la funcion
    #agregarClientes(clientes,nuevoCliente)                      #si se pone antes (se muestra al final de la lista de clietnes)
    cargarClient(nuevoCliente,nro,dni,ape,nom,fech,tip,prec)    #cargamos cliente
    agregarClientes(clientes,nuevoCliente)                     #importa el orden (se muestra al principio)

#FUNCION DE MODIFICAR CLIENTE POR SU NUMERO DE CLIENTE
def opcion2(clientes):          
    print("¿que desea modificar del cliente?")
    h=int(input("1 =numero , 2=DNI , 3=apellido, 4=nombre,5=fecha de alta, 6=tipo de servicio, 7=precio de servicio"))
    
    tam=tamanio(clientes)
    i=0
    numeroClienteBuscar=int(input("ingrese el numero de cliente que desea modificar los campos"))
    while (i<tam):

        client=recuperarClientes(clientes, i)
        if(verNumero(client)==numeroClienteBuscar):
            

            if(h==1):
                j=int(input("ingresar nuevo numero de usuario"))
                modNro(client,j)
            if (h==2):
                j=int(input("ingresar nuevo  DNI de usuario"))
                modDni(client,j)
            if(h==3): 
                j=input("ingresar nuevo apellido de usuario")
                modApe(client,j)
            if(h==4):
                j=int(input("ingresar nuevo nombre de usuario"))
                modNom(client,j)
            if(h==5):
                j=datetime.strptime(input("ingrese la fecha en el siguiente formato dd/mm/yyyy"), "%d/%m/%Y")
                modFech(client,j)
            if(h==6):
                j=["BASICO","MEDIA","PREMIUM"][int(input("ingrese el tipo de servicio 1=BASICO, 2=MEDIA, 3=PREMIUM "))-1]
                modTip(client,j)  
            if(h==7):
                j=float(input("ingrese nuevo precio de servicio"))
                modPre(client,j)                     
        else:
            print("cliente no encontrado")
        break
 
 #FUNCION DE ELIMINAR CLIENTES POR SU NUMERO DE CLIENTE
def opcion3(clientes):
    clienteAEliminar= int(input("INGRESE NUMERO DE CLIENTE A ELIMINAR: "))
    tam = tamanio(clientes)
    k = 0
    while (k < tam):
        client = recuperarClientes(clientes, k)
        if (verNumero(client) == clienteAEliminar):
            eliminarClientes(clientes, client)
            print(f"el cliente {clienteAEliminar} HA SIDO ELIMINADA CORRECTAMENTE")
            break
        k=k+1    
        
        
       
         
        


#MUESTRA EL LISTADO COMPLETO DE CLIENTES 
def opcion4(clientes):
    print("lista de clientes actuales")
    i=0
    k=1
    tam=tamanio(clientes)
    while (i<tam):
        client=recuperarClientes(clientes, i)
        print(f"Cliente#{k}",end='')
        imprimirCliente(client)
        i=i+1
        k+=1
    print(f"Total de clientes {i}")

#ELIMINA CLIENTES SEGUN EL TIPO DE SERVICIO QUE TENGAN
def opcion5(clientes):
    try:
        servicio =["BASICO","MEDIA","PREMIUM"][int(input("ingrese el tipo de servicio 1=BASICO, 2=MEDIA, 3=PREMIUM "))-1] #SEGUN EL NUMERO QUE SE PONGA SE MUESTRA EN TIPO LETRA (LISTAS EMPIEZAN EN 0)  
    except:
        print("Datos mal pasados")
    clientesEliminados = 0                       
    i = 0
    tam = tamanio(clientes)
    #Mientras haya clientes en la lista de clientes
    while i < tam:
        client = recuperarClientes(clientes, i)
        #Si se cumple la condicion se eliminara el client y se modificara el tamanio de la lista de clientes
        if verTipo(client) == servicio:
            eliminarClientes(clientes, client)
            clientesEliminados += 1           #variable para imprimir la cantidad de clientes eliminados
            tam -= 1      #reduce la lista de clientes
        else:
            #Si no cumple la condicion pasa al siguiente cliente y vuelve a verificar la condicion 
            i += 1
    #Si no se encontro al cliente
    if clientesEliminados == 0:
        print(f"No se encontraron clientes con este estado: {servicio}.")
    else:
        #Si pudo encontrarlo, imprime los clientes que se elimaron 
        print(f"Se eliminaron {clientesEliminados} clientes con este tipo de servicio: {servicio}")

#CLIENTES QUE SE ENCUENTRAN EN LOS PRIMEROS 3 MESES DESDE SU ALTA (SE LES DA UNA PROMOCION)
def opcion7(clientes):
    
    fechaActual=datetime.strptime(input("ingrese la fecha en el siguiente formato dd/mm/yyyy").strip(),"%d/%m/%Y")
    
    i=0
    tam=tamanio(clientes)
    while (i<tam):
        client=recuperarClientes(clientes, i)
        fecha=verFecha(client)
       

        if(fecha.year==fechaActual.year and fecha.month<=fechaActual.month ):
            antiguedad=(fechaActual.month-fecha.month)
            if(antiguedad<=3):
                print(" A ESTE CLIENTE SE LE DARÁ ALGUN BENEFICIO ESPECIAL")
                imprimirCliente(client)
               
        i=i+1   


#CLIENTES QUE TIENEN MAS DE 3 AÑOS DE ANTIGUEDAD
def opcion6(clientes):
    fechaActual=datetime.strptime(input("ingrese la fecha en el siguiente formato dd/mm/yyyy").strip(),"%d/%m/%Y")
    k=1
    i=0
    tam=tamanio(clientes)
    while (i<tam):                                  #verifica que haya clientes
        client=recuperarClientes(clientes, i)       #recupera/retorna un cliente
        fecha=verFecha(client)                      #fecha de alta del cliente recuperado

        antiguedad=(fechaActual.year-fecha.year)+(fechaActual.month-fecha.month)/12     #hacemos el calculo
    
        if(antiguedad>=3):                      #si es mayor o igual a 3 años
            descuento=(verPrecio(client)*0.1)   #se calcula el 10 porciento del precio de cada cliente retornado
            precioNuevo=(verPrecio(client)-descuento)   #se actualiza el precio con el descuento
            modPre(client,precioNuevo)                  #modificamos el precio
            print("======================================")
            print("======================================")
            print(f"al CLIENTE #{k} se le a descontado un 10 PORCIENTO del precio original")

            imprimirCliente(client)
            print(f"recibio un descuento de {descuento:.2f}")   # :.2f (para el float)
            print(f"se modifico el precio a {precioNuevo:.2f}")
        i=i+1
        k=k+1

#COLA DE CLIENTES QUE SE DIERON DE ALTA DEL ULTIMO MES 
            
def opcion8(clientes, cola):

    fechaActual=datetime.strptime(input("ingrese la fecha en el siguiente formato dd/mm/yyyy").strip(),"%d/%m/%Y")
    # Crear una cola auxiliar vacía
    colaAuxiliar = crearCola()
    # Copiar la cola original a la auxiliar
    copiarCola(colaAuxiliar, cola)

    j=0 
    clientesEncontradas = False
    #Mientras que la cola no este vacaia
    while not esVacia(colaAuxiliar):        #verifica si tiene o no
        client = desencolar(colaAuxiliar)  # en cada desencolacion muestra un cliente t una fecha en la variable "fecha"
        fecha = verFecha(client)            # vemos la fecha del cliente

        if fecha.year == fechaActual.year and fecha.month <= fechaActual.month:     
            antiguedad = (fechaActual.month - fecha.month)      #verificamos que sea menos/ igual a un mes
            if antiguedad <= 1:
                clientesEncontradas = True                      
                
                j += 1
                agregarClientes(clientes,client)

    print(f"Total de clientes dados de alta del ultimo mes de la cola: {j}")   #muestra la cantidad de clientes que 

    if not clientesEncontradas:
        print("No se encontraron clientes en la cola que se hayan dado de alta el ultimo mes")
    
    

    print("==================================================")

    print("LISTA DE CLIENTES DEL ULTIMO MES")

    tam = tamanio(clientes)
    
    l=0
    k = 0
    i=1
    montoRecaudado=0.0                                  #INICIAZAR EN FLOAT
    while (k < tam):
        #Mientras haya tareas en la lista de tareas 
        client = recuperarClientes(clientes, k)
        #Si se cumple la condicion se imprimira la tarea
        fecha = verFecha(client)            # vemos la fecha del cliente

        if fecha.year == fechaActual.year and fecha.month <= fechaActual.month:     
            antiguedad = (fechaActual.month - fecha.month)      #verificamos que sea menos/ igual a un mes
            if antiguedad <= 1:
                print(f"CLIENTE #{i}",end='')                      #el end es para que separe los clientes 
                imprimirCliente(client)
                
                montoRecaudado += verPrecio(client)  # Sumar el monto del cliente
                l+=1

                
        k = k + 1
        i+=1
    print(f"TOTAL DE CLIENTES DEL ULTIMO MES {l}")
    print(f"MONTO RECAUDADO EL ULTIMO MES: {montoRecaudado:.2f}")
     

    
    


clientes=crearClientes()
cola=crearCola()
generacionClientes(clientes,cantidadClientes)
generacionColaClientes(cola,cantidadClientes)

#LLAMADA AL MENU
while True:
        imprimirMenu()
        try: opcion = int(input("Seleccione una opcion: "))
        except: 
            print("Opcion invalida")
            print("presione enter para continuar")
            limpiarPantalla()
        #selecciono opcion
        match opcion:
            case 1:
                opcion1(clientes)#Agregar
            case 2:
                opcion2(clientes)#modificar
            case 3:
                opcion3(clientes)#Eliminar
            case 4:
                opcion4(clientes)#mostrar lista
            case 5:
                opcion5(clientes)
            case 6:
                opcion6(clientes)
                 
            case 7:
               opcion7(clientes)
            case 8:
                opcion8(clientes,cola)#
            case _:
                print("opcion invalida")
        espera = input("presione enter para continuar")
        limpiarPantalla()



