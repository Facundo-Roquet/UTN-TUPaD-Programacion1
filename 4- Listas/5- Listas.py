# Ejercicio 1
print("*********************************")
notas=[10,6,9,8,4,4,7,6,8,5]
estudiantes=["Axel","Ciro","Facundo","Mateo","Ana","Camila","Maria","Pablo","Ezequiel","Lorena"]
#ya aqui tenemos 2 listas, la primera con las notas y la otra con los nombres de los estudiantes.
suma=0
mayor=-1
menor=11
#Asignamos numeros a las variables que necesitamos, notese que en mayor y menor se tienen numeros imposibles en una nota de escala 0-10
for i in range(len(notas)): #podriamos usar la variable de estudiantes, son de la misma cantidad de elementos
    if notas[i]>mayor:
        mayor=notas[i]
    elif notas[i]<menor:
        menor=notas[i] #Como se ve, todo este bloque if sirve para sacar el menor y mayor
    suma=suma+notas[i] #Esta linea nos va a sumar todas las notas, para luego el promedio
    print(f"{estudiantes[i]}= {notas[i]}") #Se muestra en pantalla cada estudiante con su respectiva nota
promedio=suma/len(notas) #Conseguimos el promedio de todas las notas
print ("*********************************")
print (f"Promedio del curso = {promedio}")
print (f"Mayor nota del curso = {mayor}\nMenor nota del curso = {menor}")
#A la hora de ejecutar el programa, salen la nota de los estudiantes, el promedio de curso y la nota mayor y menor.

# Ejercicio 2
#Expresamente el ejercicio dice de dar al usuario la capacidad de eliminar elementos y no de agregar otros a parte de los primeros 5. Entiendo que es porque despues se pide las dos funciones en otro ejercicio.
lista=[]
proceder="" #Como se evalua el valor de la variable en el while, debemos definirla con ese ""
contador=0

while len(lista)!=5: #Se introducen los 5 productos
    producto=input(f"(Producto {len(lista)+1}) Introduce un producto a la lista: ")
    lista.append(producto)
lista_ordenada=sorted(lista) #esta lista es la que usamos a partir de ahora

while proceder!="N" or proceder!="n":
    i=0 #para el for
    for i in range(len(lista_ordenada)):
        print(f"*{lista_ordenada[i]}\n********")
    print("-----------------")
    if contador==0: #Mero detalle extra
        proceder=input("¿Desea eliminar algun producto de la lista? (Y/N)\n>> ")
    else:
        proceder=input("¿Desea eliminar otro producto de la lista? (Y/N)\n>> ")
    contador=contador+1 

    if proceder=="Y" or proceder=="y": #Para eliminar un producto
        if len(lista_ordenada)==0: #Si tiene 0 elementos, no se puede eliminar nada
            print("La lista esta vacia.")
            print("-----------------")
        else:
            eliminador=input("Introduzca el nombre del producto a eliminar: ")
            if eliminador in lista_ordenada:
                lista_ordenada.remove(eliminador)
                print(f"Eliminado {eliminador} de la lista.\nMostrando lista...")
                print("-----------------")
            else:
                print (f"{eliminador} no se encuentra en la lista.")
                print("-----------------")
    elif proceder=="N" or proceder=="n":
        i=0 #para el for externo al bucle while
        print("-----------------")
        break
    else: #Si usa otro caracter
        print("Debes ingresar 'Y' o 'N' para aceptar o negar, respectivamente.")
        print("-----------------")

print("Selección finalizada.\n-----------------\nLista Final:")
if len(lista_ordenada)>0:
    for i in range(len(lista_ordenada)):
        print(f"*{lista_ordenada[i]}\n********")
else:
    print("*La lista quedo completamente vacia.\n********")

# Ejercicio 3

import random
contador=0
par=[]
impar=[]
while contador!=15:
    contador=contador+1 #Para terminar el bucle
    num=random.randint(1,100) #se genera el numero
    print(num) #Se muestra
    if num%2==0: #Se clasifica el numero
        par.append(num)
    else:
        impar.append(num)
#Se muestran los resultados
print(f"-------------\nResultados:\nCantidad de numeros pares generados: {len(par)}\n Cantodad de numeros impares generados: {len(impar)}\n-------------")

# Ejercicio 4
datos=[1,3,5,3,7,1,9,5,3]
unicos=[] #Una nueva lista donde se tienen solo la primer aparicion del numero
for i in datos:  #i in datos va pasando elemento por elemento
    if i not in unicos: #Si el elemento almacenado en i no esta en unicos, se pone en la lista unicos
        unicos.append(i)
for x in range(len(unicos)):
    print(unicos[x]) #Se podria mostrar la lista directamente, pero anteriormente se dijo que debemos mostrarlo asi
#Por lo que investigue, tambien se podria hacer unicos=set(datos) y luego print(unicos)

# Ejercicio 5

#Experimente con algunas funciones y con match, parecen bastante utiles
clase=["Carola","Axel","Mateo","Fabio","Maria","Laura","Lorena","Javier"]
print("--------------")
while True: #En un principio use otra condicion, pero me di cuenta que al usar un menu interactivo, se puede usar un simple break para romper el bucle, el de la opcion 3-Salir
    i=0
    for i in range(len(clase)): #Muestra la lista y el i se reinicia
        print(f"*{clase[i]}")
    print("--------------")
    opcion=input("***-MENU-***\n1-Agregar un nuevo alumno\n2-Eliminar un alumno de la lista\n3-Salir\n>> ") #Menu simple
    if opcion.isdigit(): #isdigit verifica si es un resultado numerico
        match int(opcion): #Para un menu siento que es mas util usar esta estructura de control.
            case 1:
                nombre=input("Introduce el nombre del Alumno que quieres agregar: ")
                if nombre.isalpha(): #la funcion isalpha verifica si el nombre solo tiene caracteres alfabeticos, util ya que solo permitimos nombres.
                    clase.append(nombre)
                    print(f"{nombre} ha sido listado.")
                    print("--------------")
                else:
                    print("Solo se pueden ingresar valores alfabeticos para formar un nombre.")
                    print("--------------")
            case 2:
                if len(clase)==0:
                    print("No hay nombres listados")
                    print("--------------")
                else: 
                    nombre=input("Introduce el nombre del alumno que quieres eliminar: ")
                    if nombre not in clase:
                        print(f"{nombre} no esta listado")
                        print("--------------")
                    else:
                        clase.remove(nombre)
                        print(f"{nombre} removido.\n--------------")
            case 3:
                break
            case _: #Caso comodin, aqui de funcionalidad equivalente a si usara un case
                print("Debes introducir 1, 2 o 3 como listan las opciones.")
                print("--------------")
    else:
        print("Solo puedes introducir 1, 2 o 3.")
        print("--------------")
print("--------------\nEl listado final es:\n")
i=0
for i in range(len(clase)):
    print(f"*{clase[i]}")
print("\n--------------")

# Ejercicio 6
import random #para dar listas al azar
lista=[]
print("Lista generada\n-----------") #generamos lista
for i in range(7):
    num=random.randint(1,77)
    lista.append(num)
    print(lista[i])
print("-----------")
print("Lista invertida\n-----------") #Mostramos la lista invertida
i=0
for i in lista[::-1]:#Slicing, el primer campo se toma como start, el segundo como end y el ultimo como step, al dejar todo en blanco excepto step con -1, invertimos el orden de conteo del iterador.
    print(i)
print("-----------")

# Ejercicio 7
import random #para minimas y maximas al azar

maxim=[]
minim=[]
semana=[maxim,minim]

contador=0
while contador!=7:
    contador=contador+1
    num=random.randint(18,27)
    maxim.append(num)
    num=random.randint(10,18)
    minim.append(num)
print("____________________________\n")
print("(L) (M) (M) (J) (V) (S) (D)") #Mero grafico simple
print(f"{semana[0]}\n{semana[1]}")
#Inicialización de variables a utilizar
sumamax=0
sumamin=0
amplitudterm=0

for i in range(len(maxim)):
    #Para sacar promedios
    sumamax=sumamax+maxim[i]
    sumamin=sumamin+minim[i]
    #Para sacar el dia de mayor amplitud termica
    temp_amplitudterm=maxim[i]-minim[i]
    if temp_amplitudterm>amplitudterm:
        dia=i+1 #para saber en que dia se encontro la mayor amplitud termica
        amplitudterm=temp_amplitudterm #guardamos entonces el dia y el resultado de mayor amplitud
print("____________________________\n")
match dia: #Segun el dia, un texto diferente
    case 1:
        print(f"*El dia Lunes fue el dia con mayor amplitud termica, siendo de {amplitudterm}")
    case 2:
        print(f"*El dia Martes fue el dia con mayor amplitud termica, siendo de {amplitudterm}")
    case 3:
        print(f"*El dia Miercoles fue el dia con mayor amplitud termica, siendo de {amplitudterm}")
    case 4:
        print(f"*El dia Jueves fue el dia con mayor amplitud termica, siendo de {amplitudterm}")
    case 5:
        print(f"*El dia Viernes fue el dia con mayor amplitud termica, siendo de {amplitudterm}")
    case 6:
        print(f"*El dia Sabado fue el dia con mayor amplitud termica, siendo de {amplitudterm}")
    case 7:
        print(f"*El dia Domingo fue el dia con mayor amplitud termica, siendo de {amplitudterm}")
print(f"- El promedio de la temperatura maxima fue de {sumamax//7}\n- El promedio de la temperatura minima fue de {sumamin//7}\n")

# Ejercicio 8
materias=[[5,10,9,7,5],[2,7,6,9,10],[8,4,7,9,6]]
estudiantes=["Axel","Laura","Mateo","Fabio","Lorena"]
promaterias=[]
promestudiante=[]
sum_biologia=0
sum_lengua=0
sum_matematicas=0
#Bloque promedio de materias en general
print("----------\nPromedio de la clase\n")
for y in range(5):
    sum_biologia=sum_biologia+materias[0][y]
    sum_lengua=sum_lengua+materias[1][y]
    sum_matematicas=sum_matematicas+materias[2][y]
print(f"Biologia: {sum_biologia//5}")
print(f"Lengua: {sum_lengua//5}")
print(f"Matematica: {sum_matematicas//5}")
#Bloque promedio estudiantes
for i in range(5): #Por cada estudiante
    temp_promestudiante=0 #reinicio
    for x in range(3): #Por cada materia
        temp_promestudiante=temp_promestudiante+materias[x][i]
    promestudiante.append(temp_promestudiante//3)
print("\n*******\nPromedio del alumno entre las clases\n")
for e in range(5):
    print(f"{estudiantes[e]}: {promestudiante[e]}")
print("----------")

# Ejercicio 9
#Por el momento en el que hice este algoritmo, no sabria como hacer para que el juego reaccione a un tateti. Asi que vere como puedo implementar mas cosas en mi tiempo libre.
tablero=[
    ["-", "-", "-"], #fila 1
    ["-", "-", "-"], #fila 2
    ["-", "-", "-"]] #fila 3
jugador_actual="X"
turno=0
#bucle principal del juego
while turno < 9:
    #tablero se muestra
    print("\n--- Tablero ---")
    for fila in tablero:
        print(" | ".join(fila)) #.join permite la intercalación de un digito que esta entre el ""
        print("-------------")
    print()
    #bloque de validación de jugada
    posicion_valida=False
    while not posicion_valida:
        print(f"Turno del jugador '{jugador_actual}'.")
        #input fila
        fila_str=input("Ingresa el número de fila (1, 2, 3): ")
        #validacion columna
        if fila_str in "123": 
            fila=int(fila_str)-1
            #input columna
            columna_str=input("Ingresa el número de columna (1, 2, 3): ")
            #validacion columna
            if columna_str in "123":
                columna=int(columna_str)-1
                #si casilla esta vacia
                if tablero[fila][columna]=="-":
                    tablero[fila][columna]=jugador_actual
                    posicion_valida=True  #sale del bucle de validacion
                else:
                    print("Esa posición ya está ocupada. Intenta de nuevo.")
            else:
                print("El valor de la columna debe ser 1, 2 o 3.")
        else:
            print("El valor de la fila debe ser 1, 2 o 3.")
    #alternacion del jugador para el tipo de caracter
    if jugador_actual=="X":
        jugador_actual="O"
    else:
        jugador_actual="X"
    turno=turno+1 #suma del turno
#tablero final
print("\n---Resultado---")
for fila in tablero:
    print(" | ".join(fila))
    print("-------------")
print("Fin.")

# Ejercicio 10

ventas=[
    [10, 20, 30, 15, 25, 40, 35],  #producto 1
    [5, 15, 10, 20, 25, 30, 20],   #producto 2
    [12, 18, 22, 28, 35, 40, 50],  #producto 3
    [7, 14, 21, 28, 14, 7, 35]]    #producto 4
#Bloque de ventas totales
print("Total vendido por cada producto:")
totales_productos=[]
for i in range(len(ventas)):
    total=sum(ventas[i])
    totales_productos.append(total)
    print(f"Producto {i+1}: {total}")
#bloque de dias
print("\nVentas totales por día:")
totales_dias=[]
for j in range(len(ventas[0])):
    total_dia=sum(ventas[i][j] for i in range(len(ventas)))
    totales_dias.append(total_dia)
    print(f"Día {j+1}: {total_dia}")
dia_max = totales_dias.index(max(totales_dias))+1
print(f"\nEl día con mayores ventas fue el Día {dia_max}")
#bloque de mas vendidos
producto_max = totales_productos.index(max(totales_productos))+1
print(f"El producto más vendido en la semana fue el Producto {producto_max}")