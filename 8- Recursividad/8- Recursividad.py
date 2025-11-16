# Ejercicio 1

def factorial(num):
    if num==0: #Caso Base, si llega a 0, se deja de hacer llamadas recursivas
        return 1
    else:
        return num * factorial(num-1) #mientras que no sea 0, se siguen haciendo llamadas.
    
print(factorial(5))

# Ejercicio 2

def fibonacci(num):
    if num<=1: #Caso Base
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)
    #la primer llamada es para el anterior a num, la segunda llamada para el anterior de ese. Esto se repite hasta el caso base
num=10 #Numero ejemplo
if num<=0: #No se puede dar
    print("Valor invalido para una secuencia de Fibonacci")
else:
    print("Secuencia: ")
    for i in range(num):
        print(fibonacci(i)) #Tomamos el numero como rango y se itera en esa cantidad de numeros, sacando fibonacci individual de cada uno de ellos.
    

# Ejercicio 3

def potenciar(num,exponente):
    if exponente==0: #Caso base
        return 1
    else:
        return num*potenciar(num,exponente-1) #Se apila cada numero del exponente y el resultado de cada numero
#Supongamos que es una parte de un menu de calculadoras y se pone la opción de potenciar un numero dado
print("Elegiste calcular la potencia de un número")
num=int(input("Introduce el numero a ser potenciado\n>> "))
exponente=int(input("Introduce el exponente\n>> "))
print("Resultado:",potenciar(num,exponente))

# Ejercicio 4
def decimal_a_binario(decimal):
    if decimal<2: #Caso base, ya que 1 es 1 y 0 es 0
        return str(decimal)
    else:
        return decimal_a_binario(decimal//2)+str(decimal%2) #La division entera se concatena con el resto pasado a string
decimal=4
print(decimal_a_binario(decimal))

# Ejercicio 5

def es_palindromo(palabra):
    if len(palabra) <= 1: #Caso base si, si su longitud es 0 o 1, es simetrico
        return True
    elif palabra[0]!=palabra[-1]: #Si son diferentes, ya es un false, tecnicamente no es [::-1]
        return False
    return es_palindromo(palabra[1:-1]) #Aca comparamos las siguientes palabras
palabra="Tanazanat".lower() #todo en minusculas, importante.
print(es_palindromo(palabra))

# Ejercicio 6

def suma_digitos(n):
    if n == 0: #Caso Base
        return 0
    else:
        ultimo_digito=n%10 #asi obtenemos el ultimo digito
        restante_digitos = n // 10 #con division entera conseguimos los restantes
        return ultimo_digito + suma_digitos(restante_digitos) #Termina concatenando el ultimo digito con el resultado de una llamada
numero=1239 #por ejemplo
resultado=suma_digitos(numero) #daria 15 en este caso
print(f"La suma de los dígitos de {numero} es {resultado}") 

# Ejercicio 7

def contar_bloques(n_bloques):
    if n_bloques==1: #Caso Base
        return 1
    else:
        return n_bloques+contar_bloques(n_bloques-1) #Se suma la cantidad de bloques que estan abajo del todo y a partir de ahi va subiendo un nivel, donde se necesita un blooque menos
#Este ejercicio es una muy buena forma de poder visualizar el proceso, al menos para mi
print(contar_bloques(9)) #45 bloques en total

# Ejercicio 8

def contar_digito(numero,digito):
    if numero==0:#Si es 0, entonces no hay nada que hacer.
        return 0
    else:
        if numero%10==digito: #se divide el digito particular y se ve si es igual al digito parametro
            return 1+contar_digito(numero//10,digito) #si es, se suma y se hace otra llamada para el siguiente digito
        else:
            return contar_digito(numero//10,digito) #si no, simplemente se va al siguiente digito
print(contar_digito(122146911,1)) #Nuestro digito parametro es 1 y el numero introducido a evaluar, se imprimiria 4