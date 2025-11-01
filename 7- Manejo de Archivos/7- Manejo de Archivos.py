def mostrar_productos(): #Actividad 2
    with open("productos.txt","r") as archivo:
        encabezado=archivo.readline().strip().split(",") #en este caso, strip ya saca la "," pero ponemos split(",") igual
        lineas=archivo.readlines() #a partir de luego del encabezado
        for linea in lineas:
            partes=linea.strip().split(",") #lo mismo que en el caso anterior
            nombre=partes[0]
            precio=partes[1]
            cantidad=partes[2]
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

def introducir_producto(): #Actividad 3
    while True:
        nombre=input("Introduzca el nombre del producto\n>> ").strip().capitalize() #Siempre se capitalizara y saldra todo unido
        if nombre.isalpha():
            precio=input("Introduzca el precio del producto\n>> ").strip()
            if precio.isnumeric() and float(precio)>0:
                cantidad=input("Introduzca el stock actual del producto\n>> ").strip()
                if cantidad.isnumeric() and int(cantidad)>0: #verificaciones basicas para los numeros
                    with open("productos.txt","a") as archivo: #newline
                        archivo.write(f"\n{nombre},")
                        archivo.write(f"{precio},")
                        archivo.write(f"{cantidad}")
                    mostrar_productos() #para esto la hice una función a la actividad anterior, ya que van de la mano
                    break
                else:
                    print("Solo puede introducir un valor númerico entero y positivo")
            else:
                print("Solo se puede introducir un valor númerico positivo (incluye decimales)")
        else:
            print("Nombre invalido.")

def cargar_diccionario():#Actividad 4
    productos=[]
    with open("productos.txt","r") as archivo:
        lineas=archivo.readlines()
    encabezado=lineas[0].strip().split(",")
    for linea in lineas[1:]: #cada linea de productos con esto
        valores=linea.strip().split(",")
        producto={encabezado[i]: valores[i] for i in range(len(encabezado))}
        productos.append(producto)
    return productos

def buscar_producto():  #Actividad 5
    while True:
        producto = input("Introduce el nombre del producto\n>> ").strip().capitalize()
        if producto.isalpha():
                with open("productos.txt", "r") as archivo:
                    encabezado = archivo.readline().strip().split(",")  # encabezado
                    lineas = archivo.readlines()  # resto de líneas (productos)
                    encontrado = False
                    for linea in lineas:
                        partes = linea.strip().split(",")
                        nombre = partes[0].strip()
                        precio = partes[1].strip()
                        cantidad = partes[2].strip()
                        if nombre.lower() == producto.lower(): #lower para que no haya problemas
                            print("¡Encontrado!")
                            print(f"{nombre} vale ${precio}. Hay {cantidad} unidad/es.")
                            encontrado = True
                            break
                    if not encontrado:
                        print("El producto no se ha encontrado.")
                break
        else:
            print("Debes introducir un nombre válido.")

def guardar_archivo():#Actividad 6
    with open("productos.txt","r") as archivo:
        lineas = archivo.readlines()
    # Sobrescribir el mismo archivo con las mismas líneas
    with open("productos.txt", "w") as archivo:
        archivo.writelines(lineas)


#Las funciones atras son las actividades dadas, el siguiente menu las utiliza

while True:
    print("================= Menú de catálogo =================")
    print("Introduce el número de la acción que quieras realizar")
    print("1- Mostrar Productos\n2- Introducir Producto\n3- Diccionario de productos\n4- Buscar producto\n5- Salir")
    opcion=input(">> ").strip()
    if opcion.isnumeric() and 6>int(opcion)>0:
        match int(opcion):
            case 1: 
                mostrar_productos()
            case 2:
                introducir_producto()
            case 3:
                productos=cargar_diccionario()
                for p in productos:
                    print(p)
            case 4:
                buscar_producto()
            case 5:
                break
            case _:
                print("Este error no puede suceder")
    else:
        print("Solo puedes introducir un número de entre las opciones (1 a 5)")
guardar_archivo() 
print("Se guardó el archivo productos.txt con exito.")
print("====================================================")