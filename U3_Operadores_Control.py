#Ejercicio 1

edad=int(input("Introduce tu edad: "))
if edad>=18: #se podrían hacer otras cosas, pero esto es lo que pide la consigna explicitamente.
    print("Es mayor de edad") #el indentado se respeta de esta forma

#Ejercicio 2

nota=float(input("Introduce la nota que sacaste en el examen para saber tu condición\n Recorda que es en escala de 0 a 10 \n Tu nota: "))
if nota>10 or nota<0: #Para descartar que este fuera de rango.
    print("Numero no valido. Recuerda que se utiliza una escala de 0 a 10")
else:
    if nota>=6: #Aca el if statement que diga si está aprobado o no.
        print("Tu condicion: Aprobado.")
    else:
        print("Tu condición: Desaprobado.")

#Ejercicio 3

num=int(input("Ingrese un numero entero: "))
if num%2==1: #si da 1, es que no es par, si da 0, es par.
    print("El numero no es par. Por favor, ingrese un numero par")
else:
    print("Ha ingresado un numero par.")

#Ejercicio 4

edad=int(input("Introduzca su edad para poder ser categorizado: "))
if edad<=0: #Primer filtro
    print("Introduzca una edad valida por encima de 0")
else: #Aqui empieza la categorizacion
    if edad<12:
        print("Se te asigno a la categoria de Niño")
    elif edad>12 and edad<18:
        print("Se te asigno a la categoria de Adolescente")
    elif edad>=18 and edad<30:
        print("Se te asigno a la categoria de Adulto Joven")
    elif edad>=30:
        print("Se te asigno a la categoria de Adulto")

#Ejercicio 5

contraseña=input("Introduzca una contraseña valida que tenga entre 8 a 14 caracteres: ")
long=len(contraseña) #para tener por separado la longitud.
if long>=8 and long<=14:
    print("Ha ingresado una contraseña correcta.")
else: #Un pequeño extra de filtro, por si tiene menos o mas caracteres.
    if long<8:
        print("Su contraseña tiene menos de 8 caracteres. Introduzca una contraseña valida.")
    elif long>14:
        print("Su contraseña tiene mas de 14 caracteres. Introduzca una contraseña valida.")
    else:
        pass #En este caso no es necesario este else y pass, pero es para testear

#Ejercicio 6

from statistics import mean,median,mode #estos terminos matematicos nos serviran para realizar las operacione
import random
print("Se generara una lista de 50 numeros aleatorios que van del 1 a 100, y se mostraran las tendencia de los valores.")
lista_aleatoria=[random.randint(1,100)for i in range(50)] #una list
if mean(lista_aleatoria)>median(lista_aleatoria) and median(lista_aleatoria)>mode(lista_aleatoria):
    print(f"mean: ",mean(lista_aleatoria),"median: ",median(lista_aleatoria),"mode: ",mode(lista_aleatoria))
    print("En la lista hay un sesgo positivo")
elif mean(lista_aleatoria)<median(lista_aleatoria) and median(lista_aleatoria)<mode(lista_aleatoria):
    print(f"mean: ",mean(lista_aleatoria),"median: ",median(lista_aleatoria),"mode: ",mode(lista_aleatoria))
    print("En la lista hay un sesgo negativo")
elif mean(lista_aleatoria)==median(lista_aleatoria) and median(lista_aleatoria)==mode(lista_aleatoria):
    print(f"mean: ",mean(lista_aleatoria),"median: ",median(lista_aleatoria),"mode: ",mode(lista_aleatoria))
    print("La lista no tiene sesgo")
else: #Este else sobresale a lo qu ela consigna pide, pero por la naturaleza de la estadistica es necesario incluir que pueden salir otras combinaciones.
    print(f"mean: ",mean(lista_aleatoria),"median: ",median(lista_aleatoria),"mode: ",mode(lista_aleatoria))
    print("Valores átipicos en la lista")

#Ejercicio 7

vocales=["a","e","i","o","u"] #lista con las vocales
palabra=input("Introduce una palara o frase. Si termina en vocal, se le agregara un signo de exclamacion. \nTu palabra: ")
letra_final=palabra[-1] #en python se puede tomar letras de esta forma, y esta en negativo ya que asi se puede invertir el orden en el que python toma caracteres, siendo -1 la ultima letra siempre.
if letra_final.lower() in vocales: #verificamos si la letra esta dentro de la lista de vocales, con in. ".lower" es para hacer que todo sea minusculas y no hayan errores.
    print (f"{palabra}!")
else:
    print(palabra)

#Ejercicio 8

nombre=input("Introduce tu nombre: ") #aqui se hace una pequeña tabla para saber que se puede hacer
print("Su nombre puede imprimirse en pantalla con los siguientes efectos: \n1. Su nombre en mayusculas\n2. Su nombre en minusculas\n3. Su nombre con la primer letra en mayusculas")
opcion=int(input("Introduce 1, 2 o 3 segun la opcion que deseas que se aplique a su nombre: "))
if opcion==1: #a partir de aca es copypaste solo cambiando el efecto con upper, lower o title segun si se puso 1, 2 o 3
    print(f"{nombre.upper()}")
elif opcion==2:
    print(f"{nombre.lower()}")
elif opcion==3:
    print(f"{nombre.title()}")
else: #si el usuario pone otro numero, sale este mensaje.
    print("Introduzca una opcion entre 1, 2 o 3.") 

#Ejercicio 9

escala=float(input("Introduzca segun la escala de Richter un numero segun su magnitud y asi saber su categoria \nMagnitud de ")) #importante que sea float para poder utilizar decimales.
if escala>0 and escala<3:
    print("Muy leve (Imperceptible)")
elif escala>=3 and escala<4:
    print("Leve (Ligeramente perceptible)")
elif escala>=4 and escala<5:
    print("Moderado (Sentido por personas, pero generalmente no causa daños)")
elif escala>=5 and escala<6:
    print("Fuerte (Puede causar daño en estructuras debiles)")
elif escala>=6 and escala<7:
    print("Muy fuerte (Puede causar daños significativos)")
elif escala>=7 and escala<9: #Exactamente no hay un limite para la escala en teoria, pero se creo originalmente hasta 9
    print("Extremo (Puede causar graves daños a gran escala)")
else:
    print("Valor no valido para la escala, coloque un valor entre 0 o 9")

#Ejercicio 10 (se podria usar matches, pero usaremos if statements)

print("Este programa sirve para saber que estacion es segun tu hemisferio, mes y dia.")
hemisferio=int(input("Introduzca 0 si es del hemisferio Norte o 1 si es del hemisferio Sur: "))
mes=int(input("Introduzca el numero del mes: "))
dia=int(input("Introduzca el numero del dia: "))
#Empieza la cadena a partir de aca, se ve bastante feo y abrumador
if (mes<0 and mes>12) and dia<0:
    print("Introduzca solo valores entre 0 y 12 para mes, y entre 0 y 31 para los dias")
else:
    if mes==1: #Enero
        if dia<32:
            if hemisferio==False:
                    print("Es Invierno")
            else:
                    print("Es Verano")
        else:
            print("Marzo tiene solo 31 dias")
    elif mes==2: #Febrero
        if dia<29:
            if hemisferio==False:
                    print("Es Invierno")
            else:
                    print("Es Verano")
        else:
            print("Febrero tiene solo 28 dias")
    elif mes==3: #Marzo
        if dia<32:
            if dia>20:
                if hemisferio==False:
                    print("Es Primavera")
                else:
                    print("Es Otoño")
            else:
                if hemisferio==False:
                    print("Es Invierno")
                else:
                    print("Es Verano")
        else:
            print("Marzo solo tiene 31 dias")
    elif mes==4: #Abril
        if dia<31:
            if hemisferio==False:
                    print("Es Primavera")
            else:
                    print("Es Otoño")
        else:
            print("Abril tiene solo 30 dias")
    elif mes==5: #Mayo
        if dia<31:
            if hemisferio==False:
                    print("Es Primavera")
            else:
                    print("Es Otoño")
        else:
            print("Mayo tiene solo 30 dias")
    elif mes==6: #Junio
        if dia<31:
            if dia>20:
                if hemisferio==False:
                    print("Es Verano")
                else:
                    print("Es Invierno")
            else:
                if hemisferio==False:
                    print("Es Primavera")
                else:
                    print("Es Otoño")
        else:
            print("Junio solo tiene 30 dias")
    elif mes==7: #Julio
        if dia<32:
            if hemisferio==False:
                    print("Es Verano")
            else:
                    print("Es Invierno")
        else:
            print("Julio tiene solo 31 dias")
    elif mes==8: #Agosto
        if dia<32:
            if hemisferio==False:
                    print("Es Verano")
            else:
                    print("Es Invierno")
        else:
            print("Agosto tiene solo 31 dias")
    elif mes==9: #Septiembre
        if dia<31:
            if dia>20:
                if hemisferio==False:
                    print("Es Otoño")
                else:
                    print("Es Primavera")
            else:
                if hemisferio==False:
                    print("Es Verano")
                else:
                    print("Es Invierno")
        else:
            print("Septiembre solo tiene 30 dias")
    elif mes==10: #Octubre
        if dia<32:
            if hemisferio==False:
                    print("Es Otoño")
            else:
                    print("Es Primavera")
        else:
            print("Octubre tiene solo 31 dias")
    elif mes==11: #Noviembre
        if dia<31:
            if hemisferio==False:
                    print("Es Otoño")
            else:
                    print("Es Primavera")
        else:
            print("Noviembre tiene solo 30 dias")
    elif mes==12: #Diciembre
        if dia<32:
            if dia>20:
                if hemisferio==False:
                    print("Es Invierno")
                else:
                    print("Es Verano")
            else:
                if hemisferio==False:
                    print("Es Otoño")
                else:
                    print("Es Primavera")
        else:
            print("Diciembre solo tiene 31 dias")
