# Ejercicio 1

def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

# Ejercicio 2

def usuario_nombre(nombre: str):
    print(f"Hola {nombre}!")
nombre=input("Introduce tu nombre: ")
usuario_nombre(nombre)

# Ejercicio 3

def información_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre=input("Introduce tu nombre: ")
apellido=input("Introduce tu apellido: ")
edad=input("Introduce tu edad: ")
residencia=input("Introduce el nombre del lugar donde vives: ")

información_personal(nombre,apellido,edad,residencia)

# Ejercicio 4
import math

def calcular_area_circulo(radio):
    area=math.pi*pow(radio,2)
    return area #Al llamar la funcion, se va a devolver este resultado
def calcular_area_perimetro(radio):
    perimetro=2*math.pi*radio
    return perimetro

radio=float(input("Introduce el radio del circulo para saber su area y perimetro: "))
print(f"El circulo de radio {calcular_area_circulo(radio)} tiene un area de {calcular_area_perimetro(radio)} y un perimetro de {calcular_area_perimetro(radio)}.")

# Ejercicio 5

def segundos_a_horas(segundos):
    horas=segundos/3600
    return horas
segundos=float(input("Introduce una cantidad de segundos para saber cuanto es en horas: "))
print(f"{segundos} son {segundos_a_horas(segundos)} horas")

# Ejercicio 6

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")
numero=int(input("Introduce un numero para ver su tabla de multiplicar del uno al diez: "))
print()
tabla_multiplicar(numero)
print("\n¡Fin!")

# Ejercicio 7

def operaciones_basicas(a,b):
    print()
    print(f"Suma\n {a} + {b} = {a+b}")
    print(f"\nResta\n {a} - {b} = {a-b}")
    print(f"\nMultiplicación\n {a} x {b} = {a*b}")
    if b==0:
        print("\nNo se puede dividir por 0.")
    else:
        print(f"\nDivisión\n {a} / {b} = {a//b}") #// para division verdadera
print("Este algoritmo suma, divide, resta y multiplica dos numeros que introduzca.\nRecuerda que el orden en que coloques los numeros afecta en resta y división.\n----------------")
a=int(input("Ingresa el primer valor:"))
b=int(input("Ingresa el segundo valor: "))
print("----------------")
operaciones_basicas(a,b)
print()

# Ejercicio 8

def calcular_imc_peso(peso,altura: float):
    imc=peso/(altura**2)
    return imc

print("Introduce tu peso y altura para calcular tu indice de masa corporal.")
peso=float(input("Introduce tu peso (kg): "))
altura=float(input("Introduce tu altura (m): "))
print()
print(f"Pesando {peso} kg y midiendo {altura} m, tu indice de masa corporal es de {calcular_imc_peso(peso,altura)}")

# Ejercicio 9

def celsius_a_fahrenheit(celsius: float):
    fahrenheit=(celsius*(9/5))+32
    return fahrenheit
celsius=float(input("Introduce un valor en celsius para transformarlo en fahrenheit: "))
print(f"\n------\n\n{celsius}°C son {celsius_a_fahrenheit(celsius)}°F\n")

# Ejercicio 10

def calcular_promedio(a,b,c:float):
    promedio=(a+b+c)//3
    return promedio
print("Con este algoritmo podras calcular el promedio entre tres valores numericos que introduzcas\n*")
a=float(input("Introduce tu primer valor: "))
b=float(input("Introduce tu segundo valor: "))
c=float(input("Introduce el ultimo valor: "))
print(f"El promedio entre {a} ,{b} y {c} es de {calcular_promedio(a,b,c)} aprox")