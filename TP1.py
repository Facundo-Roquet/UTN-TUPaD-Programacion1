#Ejercicio 1: "Hola Mundo"

print("Hello world!")

#Ejercicio 2: Saludo simple

nombre=input("Introduce tu nombre: ")
print(f"Bienvenido {nombre}!")

#Ejercicio 3: Autosaludador

nombre=input("Introduce tus nombres: ")
apellido=input("Introduce tus apellidos: ")
edad=input("Introduce tu edad: ")
nacionalidad=input("Introduce el nombre del país en el que vives: ")
print(f"¡Hola! Soy {nombre} {apellido}, tengo {edad} años y soy de {nacionalidad}. Un gusto.")

#Ejercicio 4: Radio Circulo

import math #Para poder usar el numero PI, utilizamos math.pi
radio=float(input("Introduce el radio del circulo en cuestion: "))
area=math.pi*radio**2 #no hace falta parentesis ya que la potencia siempre se resuelve primero
perimetro=2*math.pi*radio
print(f"Los resultados son:\n Area: {area}cm\n Perimetro: {perimetro}cm")
#A la hora de mostrar los resultados, podriamos poner {round(area)} para redondear el resultado, lo mismo con perimetro

#Ejercicio 5: Segundos a Horas

segundos=int(input("Introduzca una cantidad de segundos para ver a cuantas horas equivale:")) #para que no lo tome como string, fuerzo el int
horas=segundos/3600
print(f"{segundos} segundos equivale a {horas} horas")

#Ejercicio 6: Tabla de Multiplicar

num=int(input("Introduzca un numero para mostrar su tabla de multiplicar: "))
print(f"----Tabla del {num}----\n 1 x {num} = {num*1}\n 2 x {num} = {num*2}\n 3 x {num} = {num*3}\n 4 x {num} = {num*4}\n 5 x {num} = {num*5}\n 6 x {num} = {num*6}\n 7 x {num} = {num*7}\n 8 x {num} = {num*8}\n 9 x {num} = {num*9}\n 10 x {num} = {num*10}\n --------------")
#Se podría poner todo esto en diferentes lineas de codigo, pero estaba testeando las fstrings.
#También se podría hacer en menos lineas con un bucle, pero estamos viendo secuenciales.

#Ejercicio 7: Operaciones Generales

num1=int(input("Introduce el primer numero: "))
num2=int(input("Introduce el segundo numero: "))
if num1==0 or num2==0:
    print("Porfavor, selecciona solo numeros que no sean 0")
else:
    print(f"**Resultados**\n{num1} + {num2} = {num1+num2}\n{num1} - {num2} = {num1-num2}\n{num1} x {num2} = {num1*num2}\n{num1} ÷ {num2} = {num1/num2}\n")
#interesante el uso de if statements

#Ejercicio 8: Calculadora de IMC

print("-------------Calculadora de Indice de Masa Corporal-------------")
kg=float(input("Introduce tu peso en kilogramos: "))
m=float(input("Introduce cuanto mides en metros: "))
imc=kg/(m**2)
print(f"Tu Indice de Masa Corporal es de {imc:.2f}") #dentro de los corchetes, lo que hice es para acortar la cantidad de decimales que se muestran, siendo necesario solo ver 2 en lugar de 8.

#Ejercicio 9: Celsius a Farenheit

celsius=float(input("Introduce un valor de temperatura en celsius para ser convertido a Farenheit: "))
farenheit=celsius*(9/5)+32
print(f"El resultado en Farenheit es: {farenheit} °F")

#Ejercicio 10: Promedio de Tres Numeros

print("Introduce 3 numeros para conseguir el promedio entre ellos.")
print("-----------")
num1=int(input("Introduce el primer numero: "))
num2=int(input("Introduce el segundo numero: "))
num3=int(input("Introduce el tercer numero: "))
print(f"El promedio es: {(num1+num2+num3)/3:.2f}")