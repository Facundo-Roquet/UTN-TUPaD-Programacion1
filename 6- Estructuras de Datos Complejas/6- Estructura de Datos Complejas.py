# Ejercicio 1, 2 y 3

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
print(precios_frutas)
print()

precios_frutas["Naranja"]=1200 #Este bloque de aqui seria el ejercicio 1
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300
print(precios_frutas)
print()

precios_frutas['Banana']=1330 #Este bloque de aqui seria el ejercicio 2
precios_frutas['Manzana']=1700
precios_frutas['Melón']=2800
print(precios_frutas)
print()

lista_frutas=list(precios_frutas.keys()) #Ejercicio 3
print(lista_frutas) #Basicamente, definimos que el resultado de la función keys, es una lista, se crea la lista con las keys y listo.

#Ejercicio 4

contactos={} #iniciamos diccionario
print("Este algoritmo es una agenda de 5 contactos. Se te va a pedir que coloques los nombres y numeros de 5 contactos que quieras guardar.")
for i in range(0,5):
    clave=str(input("Introduce el nombre del contacto: "))
    valor=str(input("Introduce el numero del contacto: "))
    contactos[clave]=valor #se añade un contacto con el valor conseguido
    print(contactos) #se muestra como va la lista(diccionario) de contactos
print()
lista_contactos=list(contactos.keys())
while True: #simple menu para el usuario
    print("¿Deseas verificar el numero de un contacto?\n1- Si\n2- No")
    decision=int(input(">> "))
    print("************")
    if decision==1:
        clave=input(f"Mostrando lista de contactos...\n{lista_contactos}\n-----------\nIntroduce el nombre de un contacto para saber su numero: ")
        print("-----------\n")
        if clave in contactos: #verifica si la key esta en contactos
            print(f"El numero del contacto '{clave}' es {contactos[clave]}")
        else:
            print("El nombre no existe en la lista de contactos.")
        print("************")
        pass
    elif decision==2:
        print("*Finalizando algoritmo*")
        break
    else:
        print("Solo puedes introducir 1 o 2.")

# Ejercicio 5

frase=input("Introduce una frase\n>> ").lower() #lower para que sea todo minusculas
palabras=frase.split() #sacamos espacios
recuento={} #diccionario

def contar_palabras(palabras:list): #cuenta todas las palabras 
    for i in range(len(palabras)): #pasa por toda la lista
        temp=palabras[i] #para mayor claridad al saber que entra en el diccionario
        if temp not in recuento: #La primera vez que aparece el elemento
            recuento[temp]=1 #Se crea una key en el diccionario
        else:
            if temp in recuento:
                recuento[temp]+=1 #Se suma a la key existente el valor
    return recuento #Se devuelve el diccionario ya creado

print(f"Recuento de Palabras: {contar_palabras(palabras)}") #Aparece el diccionario
palabras_unicas=set(recuento.keys()) #creamos set
print(f"Lista de palabras: {palabras_unicas}") #Aparece el set

# Ejercicio 6

lista_notas=[]
diccionario={}
primer_contador=0
print("------------------")

while primer_contador!=3: #Tres nombres
    primer_contador+=1
    lista_notas.clear() #Reiniciar la lista en cada bucle
    alumno=str(input(f"**Introduce el nombre del alumno {primer_contador}\n>>  ")).lower() #variable temporal para la key
    if alumno not in diccionario:
        print()
        segundo_contador=0
        while segundo_contador!=3: #Tres notas
            segundo_contador+=1 #conviene que sea al principio ya que en caso de error se saca uno
            nota=int(input(f"Introduce la nota del trimestre {segundo_contador} de {alumno}: ")) #variable temporal para la lista de values que se convierten en tupla
            if 10>=nota>=0: #tipica nota de 0 a 10
                lista_notas.append(nota) #agregamos la nota a la lista
            else:
                print("Debes colocar un valor entero entre 0 y 10")
                segundo_contador-=1 #para retroceder un paso
        diccionario[alumno]=tuple(lista_notas) #Una vez los 3 nombre con su respectiva lista, transformamos aqui mismo la lista en tupla
    else:
        print()
        print("Ese nombre ya fue introducido.")
        primer_contador-=1


print("------------------\n")
for llave in diccionario: #se itera cada key dentro del diccionario, me facilita la vida en cuanto indexacion
    suma=sum(diccionario[llave]) #contenedor que va variando segun la key/tupla a sumar
    print(f"Promedio redondeado de {llave}= {suma//3}") #Se muestra promedio aprox
    print()
print("------------------")

# Ejercicio 7

#Entiendo que son sets de numeros reperesentando el numero del estudiante en un sistema
#es decir: alumno 1, alumno 2...

alumnos={"1","2","3","4","5","6","7","8","9","10"} #Todos los alumnos
parcial1={"1","2","4","5","8","9"}
parcial2={"3","4","5","6","7","8"}


aprobo_ambos=parcial1&parcial2 #interseccion (.intersection() )
aprobo_uno=parcial1^parcial2 #^ diferencia simetrica(.symmetric_difference() )

total_aprobados=aprobo_ambos.union(aprobo_uno) #total que aprobaron algo
total_desaprobado=alumnos-total_aprobados #(.difference() )

print()
print(f"Todos los alumnos que participan en la clase\n{alumnos}\n**********")
print(f"Alumnos que aprobaron el primer parcial\n{parcial1}\n-")
print(f"Alumnos que aprobaron el segundo parcial\n{parcial2}\n**********")

print()
print(f"Condiciones del alumno\n**********")
print(f"Aprobo ambos parciales\n{aprobo_ambos}\n-")
print(f"Aprobo solo un parcial\n{aprobo_uno}\n**********")

print(f"Todos lo que aprobaron al menos un parcial\n{total_aprobados}\n-")
print(f"Todos los alumnos que no aprobaron ningun parcial\n{total_desaprobado}\n**********")
print()

# Ejercicio 8

productos_stock={} #nombre:stock

while True: #Bucle de Menú

    print("**Menú de manejo de Stock**\n1- Consultar stock de un producto\n2- Agregar o quitar unidades al stock de un producto\n3- Agregar un nuevo producto\n4- Salir")
    print()
    opcion=(input(">> ")).strip() #para no dejar espacios
    
    if opcion.isnumeric()==True: #aprovechamos que se convirtio en string para verificar si es un numero
        opcion=int(opcion)
        print("------------------")
        match opcion:

            case 1: #Consultar stock de un producto
                if productos_stock: #verifica si hay o no contenidos
                    producto=input(f"\nIntroduce el nombre del producto\n>> ").capitalize().strip() #para que todos sean similares
                    if producto in productos_stock: #si el producto introducido si esta en la lista
                        print(f"Hay {productos_stock[producto]} unidades en el stock de {producto}")
                        print("-\n")
                    else:
                        print(f"El nombre {producto} no es un producto registrado.\n-\n")
                else: #si no hay nada
                    print("Todavia no hay productos registrados")
                    print("-\n")

            case 2: #Agregar o quitar unidades al stock de un producto
                producto=input("Introduce el nombre del producto al que quieres agregar o quitar unidades\n>> ")
                if producto in productos_stock:

                    stock=input(f"Introduce el numero de unidades que quieres agregar o quitar al stock de {producto}\n>> ").strip()
                    if stock.isnumeric():
                        stock=int(stock)
                        productos_stock[producto]+=stock #se suma el value anterior por el del stock introducido
                        print(f"El producto {producto} se le ha alterado con {stock} unidad/des.\nTiene un total de {productos_stock[producto]} unidades\n-\n")
                        print("-\n")
                    else:
                        print("Debes introducir un valor numerico.\n-\n")
                else:
                    print(f"El producto {producto} no esta registrado.\n-\n")

            case 3: #Agregar un nuevo producto
                producto=input("Introduce el nombre del producto que quieres ingresar\n>> ").capitalize().strip()
                if producto not in productos_stock: #Verifica si no hay una clave asi
                    productos_stock[producto]=0
                    print(f"Se agrego correctamente el producto {producto} y se le asigno de base 0 unidades en su stock")
                    print("-\n")
                else: #Si la key ya existe, muestra tambien su value
                    print(f"El producto que desea ingresar ya está registrado y tiene {productos_stock[producto]} unidad/es\n-\n")

            case 4: #Salir
                print("Finalizando menú...\n------------------")
                break

            case _:
                print("Introduce un valor permitido (1,2,3 o 4)") #Si es numerico pero no esta dentro de los valores, comodin del match.
    else: #Si no es numerico, se vuelve y ya
        print("Debes introducir un valor numerico.")

# Ejercicio 9

#un diccionario prehecho
agenda={
    ("lunes","10:00"):"Reunion",
    ("martes","15:00"):"Clase de Ingles",
    ("miercoles","13:40"):"Educacion Fisica",
    ("jueves","12:00"):"Almuerzo con familiares",
    ("viernes","8:00"):"Viaje de Estudio"
}
def sacar_dia():
    nombres=[]
    lista_agenda=list(agenda.keys())
    for elemento in lista_agenda:
        for i in elemento:
            if i==elemento[0]:
                nombres.append(i)
    return nombres

def sacar_tiempo():
    tiempo=[]
    lista_agenda=list(agenda.keys())
    for elemento in lista_agenda:
        for i in elemento:
            if i==elemento[1]:
                tiempo.append(i)
    return tiempo

#utilizo las anteriores funciones en parte para practicarlas un poco, pero tambien considerando de que si se hicieran tuplas diferentes con la misma forma, las funciones funcionarian correctamente.
while True:
    opcion=int(input("1- Verificar horario\n2- Salir\n>> "))
    if opcion==1:
        dia=input("Introduce el día que quieres verificar\n>> ").strip().lower()
        if dia in sacar_dia():
            hora=input(f"Introduce la hora que quieres verificar del día {dia}\n>> ")
            if hora in sacar_tiempo():
                print(f"El día {dia} a las {hora} hs tiene como actividad agendada '{agenda[(dia,hora)]}'.\n-\n")
            else:
                print(f"El día {dia} a las {hora} hs no tiene ninguna actividad agendada.\n-\n")
        else:
            print(f"Solo tiene agendado los siguientes días: {sacar_dia()}")

    elif opcion==2:
        print("Finalizando menú...")
        break
    else:
        print("Introduce el numero 1 o 2.\n-\n-")

# Ejercicio 10

original={"Argentina":"Buenos Aires","Chile":"Santiago","Francia":"París"}
print(F"Original: {original}")

def invertir_diccionario(original:dict):
    invertida={} #creamos el diccionario invertido
    pais=list(original.keys())
    capital=list(original.values())
    for i in range(len(original)):
        invertida[capital[i]]=pais[i]
    return invertida

print(f"Invertida: {invertir_diccionario(original)}")