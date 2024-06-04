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

    
    for nro,dni,ape,nom,fech,tip,prec in zip(listadoNumeros,listadoDni,listadoApelldo,listadoNombres,listadoFechas,listadoTipo,listadoPrecios): #guarda los datos en orden segun esten separados por la ,
        nuevoCliente=crearClient()  #declaramos la funcino
        cargarClient(nuevoCliente,nro,dni,ape,nom,fech,tip,prec)    #cargamos el cliente
        agregarClientes(clientes,nuevoCliente)                      #agregamos el cliente






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
        return                      #para evitar que pinche el programa si ponen cualquier cosa             
    
    nuevoCliente=crearClient()                                  #declaramos la funcion
    
    cargarClient(nuevoCliente,nro,dni,ape,nom,fech,tip,prec)    #cargamos cliente
    agregarClientes(clientes,nuevoCliente)                     #importa el orden (se muestra al principio)

#FUNCION DE MODIFICAR CLIENTE POR SU NUMERO DE CLIENTE
def opcion2(clientes):
    print("¿Qué desea modificar del cliente?")
    try:
        h = int(input("1 = número, 2 = DNI, 3 = apellido, 4 = nombre, 5 = fecha de alta, 6 = tipo de servicio, 7 = precio de servicio: "))
    except ValueError:
        print("Datos mal ingresados")
        return
    
    try:
        numeroClienteBuscar = int(input("Ingrese el número de cliente que desea modificar los campos: "))
    except ValueError:
        print("Ingreso mal el número de cliente")
        return

    clienteEncontrado = False
    i = 0
    while i < tamanio(clientes):
        client = recuperarClientes(clientes, i + 1)
        if verNumero(client) == numeroClienteBuscar:
            clienteEncontrado = True
            try:
                if h == 1:
                    j = int(input("Ingresar nuevo número de usuario: "))
                    modNro(client, j)
                elif h == 2:
                    j = int(input("Ingresar nuevo DNI de usuario: "))
                    modDni(client, j)
                elif h == 3:
                    j = input("Ingresar nuevo apellido de usuario: ")
                    modApe(client, j)
                elif h == 4:
                    j = input("Ingresar nuevo nombre de usuario: ")  # Corregido a input en vez de int
                    modNom(client, j)
                elif h == 5:
                    j = datetime.strptime(input("Ingrese la fecha en el siguiente formato dd/mm/yyyy: "), "%d/%m/%Y")
                    modFech(client, j)
                elif h == 6:
                    j = ["BÁSICO", "MEDIA", "PREMIUM"][int(input("Ingrese el tipo de servicio 1 = BÁSICO, 2 = MEDIA, 3 = PREMIUM: ")) - 1]
                    modTip(client, j)
                elif h == 7:
                    j = float(input("Ingrese nuevo precio de servicio: "))
                    modPre(client, j)
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Datos mal pasados")
                return
            break
        i += 1
    
    if not clienteEncontrado:
        print("Cliente no encontrado")
 #FUNCION DE ELIMINAR CLIENTES POR SU NUMERO DE CLIENTE
def opcion3(clientes):
    try:
        clienteAEliminar= int(input("INGRESE NUMERO DE CLIENTE A ELIMINAR: "))
    except:
        print("No ingreso correctamente el numero de cliente que desea eliminar")
        return    
   
    k = 0
    while (k < tamanio(clientes)):
        client = recuperarClientes(clientes, k+1)
        if (verNumero(client) == clienteAEliminar):
            eliminarClientes(clientes, client)
            print(f"el cliente {clienteAEliminar} HA SIDO ELIMINADA CORRECTAMENTE")
            
        k=k+1    
        
        
       
         
        


#MUESTRA EL LISTADO COMPLETO DE CLIENTES 
def opcion4(clientes):
    print("lista de clientes actuales")
    i=0
    k=1
    
    while (i<tamanio(clientes)):
        client=recuperarClientes(clientes, i+1)
        print(f"Cliente#{k}",end='')
        imprimirCliente(client)
        i=i+1
        k+=1
    print(f"Total de clientes {k-1}")

#ELIMINA CLIENTES SEGUN EL TIPO DE SERVICIO QUE TENGAN
def opcion5(clientes):
    try:
        servicio =["BASICO","MEDIA","PREMIUM"][int(input("ingrese el tipo de servicio 1=BASICO, 2=MEDIA, 3=PREMIUM "))-1] #SEGUN EL NUMERO QUE SE PONGA SE MUESTRA EN TIPO LETRA (LISTAS EMPIEZAN EN 0)  
    except:
        print("Datos mal pasados")
        return
    clientesEliminados = 0                       
    i = 1
    
    #Mientras haya clientes en la lista de clientes
    while (i < tamanio(clientes)):
        client = recuperarClientes(clientes, i+1)
        #Si se cumple la condicion se eliminara el client y se modificara el tamanio de la lista de clientes
        if verTipo(client) == servicio:
            eliminarClientes(clientes, client)
            clientesEliminados += 1           #variable para imprimir la cantidad de clientes eliminados
                 #reduce la lista de clientes
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
    try:
        fechaActual = datetime.strptime(input("Ingrese la fecha en el siguiente formato dd/mm/yyyy: ").strip(), "%d/%m/%Y")
    except ValueError:
        print("Formato de fecha incorrecto. Inténtelo de nuevo.")
        return
    
    dias_promocion = 90  # 90 días para los primeros 3 meses
    
    i = 0
    clientes_promocion = 0          
    
    while (i < tamanio(clientes)):
        client = recuperarClientes(clientes, i+1)
        fecha_alta = verFecha(client)
        
        diferencia_dias = (fechaActual - fecha_alta).days
        if 0 <= diferencia_dias <= dias_promocion:                  #si no lo pongo con los parametros no anda correctamente xd
            print("Este cliente se encuentra en los primeros 3 meses desde su alta (90 días).")
            imprimirCliente(client)
            clientes_promocion += 1
        
        i += 1
    
    if clientes_promocion == 0:                 
        print("No se encontraron clientes en los primeros 3 meses desde su alta.")
    else:
        print(f"Total de clientes con promoción: {clientes_promocion}")


#CLIENTES QUE TIENEN MAS DE 3 AÑOS DE ANTIGUEDAD
def opcion6(clientes):
    try:
        fechaActual=datetime.strptime(input("ingrese la fecha en el siguiente formato dd/mm/yyyy").strip(),"%d/%m/%Y")
    except ValueError:
        print("Datos mal pasados")
        return   
    k=1
    i=0
    diasDescuento= 1095                  #3 años 
    clientes_promocion=0
    while (i<tamanio(clientes)):                       #verifica que haya clientes
        client=recuperarClientes(clientes, i+1)       #recupera/retorna un cliente
        fecha=verFecha(client)                      #fecha de alta del cliente recuperado
        
        if (fecha<fechaActual):
            antiguedad= (fechaActual-fecha).days    #hacemos el calculo
        
            if(antiguedad>=diasDescuento):                      #si es mayor o igual a 3 años
                descuento=(verPrecio(client)*0.1)   #se calcula el 10 porciento del precio de cada cliente retornado
                precioNuevo=(verPrecio(client)-descuento)   #se actualiza el precio con el descuento
                modPre(client,precioNuevo)                  #modificamos el precio
                print("======================================")
                print("======================================")
                print(f"al CLIENTE #{k} se le a descontado un 10 PORCIENTO del precio original")

                imprimirCliente(client)
                print(f"recibio un descuento de {descuento:.2f}")   # :.2f (para el float)
                print(f"se modifico el precio a {precioNuevo:.2f}")
                clientes_promocion+=1
        i=i+1
        k=k+1
    if clientes_promocion == 0:                 
        print("No se encontraron clientes con antiguedad mayor/igual a 3 años.")
    else:
        print(f"Total de clientes con promoción: {clientes_promocion}")    
#COLA DE CLIENTES QUE SE DIERON DE ALTA DEL ULTIMO MES 
            
def opcion8(clientes, cola):
    try:
        fechaActual = datetime.strptime(input("Ingrese la fecha en el siguiente formato dd/mm/yyyy: ").strip(), "%d/%m/%Y")
    except ValueError:
        print("Formato de fecha incorrecto. Inténtelo de nuevo.")
        return
    
    clientesEncontradas = 0
    j = 0

    while j < tamanio(clientes):
        client = recuperarClientes(clientes, j + 1)
        fecha = verFecha(client)  
        
        if fecha < fechaActual:                     #si la fecha del cliente es mejor a la fecha actual
            diferencia = (fechaActual - fecha).days     #calculamos la diferencia en dias
            if 0 < diferencia <= 31:                    #31 dias = 1 mes
                encolar(cola, client)                   
                clientesEncontradas += 1  
        
        j += 1

    if clientesEncontradas == 0:
        print("No hay clientes dados de alta dentro del último mes")
    else:
        print(f"Total de clientes encontrados que se cargaron a la cola: {clientesEncontradas}")

    print("==================================================")

    l = 0
    i = 1
    montoRecaudado = 0.0  
    auxiliar = crearCola()
    copiarCola(auxiliar, cola)

    while not esVacia(auxiliar):        #si la cola auxiliar no esta vacia
        client = desencolar(auxiliar)   #empezamos a recorrer la cola
        fecha = verFecha(client)

        if fecha < fechaActual:
            diferencia = (fechaActual - fecha).days
            if 0 < diferencia <= 31:
                print(f"CLIENTE #{i}", end='')  
                imprimirCliente(client)
                
                montoRecaudado += verPrecio(client)  
                l += 1
        
        i += 1

    print(f"TOTAL DE CLIENTES DEL ÚLTIMO MES: {l}")
    print(f"MONTO RECAUDADO EL ÚLTIMO MES: {montoRecaudado:.2f}")
    
                                      
    
     

    
    


clientes=crearClientes()
cola=crearCola()
generacionClientes(clientes,cantidadClientes)


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
                opcion5(clientes)#
            case 6:
                opcion6(clientes)#
                 
            case 7:
               opcion7(clientes)#
            case 8:
                opcion8(clientes,cola)# cola de clientes del ultimo mes
            case _:
                print("opcion invalida")
        espera = input("presione enter para continuar")
        limpiarPantalla()



