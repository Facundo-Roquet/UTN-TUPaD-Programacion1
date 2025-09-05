#Ejercicio 1

for i in range(101): #101, ya que si pusieramos 100, el iterador llegaria a 100 y terminaria el bucle, sin mostrar el propio 100
    print (i)

#Ejercicio 2

num=int(input("Introduce un numero entero para que el programa cuente su cantidad de digitos: "))
print(len(str(num))) #inicialmente es un interger, lo pasamos a string y utilizamos la funcion len() para sacar su longitud de digitos
#Es cierto que no utiliza bucles, pero realmente no es necesario hacerlo.

#Ejercicio 3

print("Este programa sumara todos los numeros enteros que hay entre un valor que introduzcas y otro.\nPondra como numero incicial el valor más pequeño y su final, el mas grande.")
num1=int(input("Introduce el primer numero entero: "))
num2=int(input("Introduce el segundo numero entero: "))

if num1<num2 and num2!=num1+1:  #Notese que num2!=num1+1 es para que el programa trate esos casos de diferencia de 1 como else.
    adelantador=num1+1 #El adelantador va a servir para que no haga la suma num1+num1
    for i in range(adelantador,num2):
        print(f"{num1} + {i}")
        num1=num1+i
        print(f"= {num1}")
        print("__________") #mera division para mayor lectura en el output
elif num1>num2 and num1!=num2+1: #Copia del otro pero utilizamos al num2 como inicio
    adelantador=num2+1 #lo mismo pero con el num2
    for i in range(adelantador,num1):
        print(f"{num2} + {i}")
        num2=num2+i
        print(f"= {num2}")
        print("__________")
else: #Para cuando ambos numeros son iguales o hay una diferencia de 1
    print(f"No hay numeros enteros entre {num1} y {num2}.")

#Ejercicio 4

print("Este programa sumara en secuencia todos los numeros enteros que introduzcas y los mostrara en la terminal.\nSi introduces un 0, se finalizara el programa.")

num=int(input("Introduce un numero: "))
sumador=0 #Necesario para contener los cambios de la sumas secuenciales
while num!=0: #Si llega a ser 0, se termina el bucle
    if sumador!=0: #Simple if statement para filtrar si es el primer intento o no, en caso de que lo sea, nos evitamos que salga num + 0 (que seria el sumador sin actualizarse)
        print(f"------\n{num} + {sumador}")
        sumador=num+sumador
        print(f"= {sumador}")
    else:
        print(f"Tu numero inicial {num}\n------------")
        sumador=num+sumador
    num=int(input("Introduce un numero: "))
print("*************\nEl programa finalizo al introducir 0") #Para dar cuenta que el programa finalizo

#Ejercicio 5

import random #importante para usar random.randint
print("Esto es un juego de adivinacion donde debes introducir el mismo numero que el programa selecciono entre el 0 y el 9")
num_aleatorio=random.randint(0,9) #Tenia un problema donde esta variable no podia ser comparada en el while, pero era un descuido de que lo habia puesto con [], o sea que era una lista.
contador=0 #Apenas empiece el bucle, va a ser 1
num_usuario=-1 #Un valor imposible para poder entrar al while. Solo es para definir la variable
while num_aleatorio!=num_usuario:
    contador=contador+1 #contador simple fuera e los if
    if contador==1:
        num_usuario=int(input(f"*******\nIntroduce tu numero inicial: ")) #No es necesario, pero es por mera presentacion
    else:
        num_usuario=int(input(f"Su numero: {num_aleatorio}\n-------\n(Intento {contador}) Introduce un numero: ")) #Esta bueno que te muestre lo que habia elegido el programa
    if num_usuario<0 or num_usuario>9: #podria ser un elif entre media de los otros if, pero asi me parece mas comodo para entender.
        print("Solo se permiten numeros enteros entre el 0 y el 9.") #Cuenta como intento
    num_aleatorio=random.randint(0,9) #lo random en va a pasar al final en cualquier caso
print(f"Su numero: {num_aleatorio}\n*******\n¡Felicidades! coincidieron en el {num_usuario}.\nEn total, la cantidad de intentos para adivinar su numero fueron {contador} intentos.")
#siempre termina con lo mismo

#Ejercicio 6

i=99 #el iterador nos servira para el print y la division condicionak
print("¡Comienza!\n--------")
for i in range (99,0,-1): #empieza en 99 (para no mostrar 100), termina en 0 con una actualizacion de -1 para su orden decreciente
    if i%2==0:
        print(i)
print("--------\n¡Final!")

#Ejercicio 7

num=int(input("Este programa suma todos los numeros comprendidos entre 0 y un numero entero positivo introducido.\nIntroduce tu numero: "))
suma=0 #Nuestro contenedor para lo que se vaya sumando
while num<=0: #Nos evitamos a que se tenga que reiniciar si se pone un valor invalido
    num=int(input("Solo se pueden introducir numeros enteros por encima de 0\nIntroduce un numero valido: "))
if num==1: #No tiene sentido iniciar un bucle si no hay que hacer sumas
    print(f"No hay numeros enteros entre 0 y {num}")
elif num==2: #Se simula lo que haria el bucle y muestra que equivale a 1
    print(f"n0+1\n= 1\n***************\n¡Final!\nEl resultado final fue 1\n***************")
else: #Aqui entran todo los demas casos 
    for i in range(1,num): #-1 ya que nos pide que sumemos los numeros entre 0 y x, no incluyendo la x
        print(f"--------\n{suma}+{i}")
        suma=suma+i #esta al medio para que se pueda mostrar los valores anteriores en el print de la linea 12, mientras que en la linea 14 se muestre el resultado de dicha suma
        print(f"= {suma}")
    print(f"***************\n¡Final!\nEl resultado final fue {suma}\n***************")

#Ejercicio 8

#Inicializamos los contenedores que vamos a usar.
contador_ceros=0
contador_negativos=0
contador_positivos=0
contador_par=0
contador_impar=0

print("********\nEsto es un contador de numeros pares, impares, positivos y negativos.\nSe te pedira introducir 100 numeros y el programa se encargara de contar cuantos hay de cada\n**********")
for i in range(0,100): #Basta con cambiar el ultimo numero dentro de rango para cambiar la cantidad de numeros que ponemos
    usernum=int(input(f"(Input {i+1}) Ingresa un numero entero: "))
    if usernum==0: #nos servira para evitar que pase por todas las otras condiciones
        contador_ceros=contador_ceros+1 #Es neutral
        contador_par=contador_par+1 #Ya que 0 es par
    else: #Prefiero esta forma antes que hacerlos elif. Siento que los bloques quedan mas diferenciados
        #Bloque filtrador de negativos y positivos
        if usernum<0:
            contador_negativos=contador_negativos+1
        else: 
            contador_positivos=contador_positivos+1
        #Bloque filtrador de pares e impares
        if usernum%2==0:
            contador_par=contador_par+1
        else:
            contador_impar=contador_impar+1
print(f"*******\nPositivos={contador_positivos}\nNegativos={contador_negativos}\nPar={contador_par}\nImpar={contador_impar}\nCeros={contador_ceros}\n*******\n¡Final!")

#Ejercicio 9

from statistics import mean #De la anterior unidad, nos servira nuevamente
lista=[] #Una lista para contener todos los numeros
print(f"********\nEste programa sacara el promedio de 100 numeros enteros que introduzcas\n********")
for i in range (0,100): #Podemos cambiar la cantidad de numeros que podemos introducir, cambiando la iteracion final
    num=int(input(f"(Input {i+1}) Introduce un numero entero: "))
    lista.append(num) #.append sirve para agregar al final de una lista ya existente el contenido que haya entre ()
print(f"*********\n El promedio entre todos esos numeros es de: {mean(lista)}\n********") #Utilizamos mean (promedio)

#Ejercicio 10

num=int(input("Introduce un numero y el programa dara vuelta el orden de digitos\nTu numero:"))
num=str(num) #Utilizaremos len, asi que lo pasamos a string. Antes pedimos int para que no se puedan introducir cosas que no sean numeros enteros
invertido=num[::-1] # utilizando slices para la inversion del string[inicio:final:actualizacion], donde dejamos todo en blanco para que pase de principio a fin, a razon de -1, o sea, un paso pero desde el final hasta el principio.
print(f"El numero invertido es: {invertido}")
#Aunque es cierto que tampoco utilizamos un bucle, en parte es porque no es necesario y utilizar esta version simplifica todo y da los mismos resultados de la consigna
#En caso de usar un bucle (tomaria un for, de iterador final len(num)), el proceso se complica innecesariamente, teniendo que tomar num y extraerle sus digitos con modular y luego multiplicar los digitos por un multplicador de 10 que a su vez se multiplique por 10 en cada iteracion
