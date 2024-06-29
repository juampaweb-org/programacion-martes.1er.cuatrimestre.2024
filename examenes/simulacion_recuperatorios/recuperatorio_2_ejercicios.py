
"""



############# EJERCICIO #############

# Utilizando el modulo platform haga lo siguiente:

# Imprima en pantalla el nombre del sistema operativo que se está ejecutando.
# Imprima en pantalla la versión del sistema operativo que se está ejecutando.
# Imprima en pantalla el procesador que está siendo utilizado.








############# EJERCICIO #############

# Utilizando el modulo os haga lo siguiente:
# Liste por pantalla todos los directorios y archivos de un directorio definido.


import os

# directorio definido
directorio = "."

# listar directorios y archivos
for elemento in os.listdir(directorio):
    print(elemento)









############# EJERCICIO #############

# Utilizando el módulo datetime
# guardar en una variable la fecha actual y la hora actual.
# Ahora guardar en otra variable un string con la fecha y hora actual en el siguiente formato:
# "2020-12-20 10:15:30"
# Convertir ese string a un objeto datetime.



import datetime

fecha_hora_actual = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")










############# EJERCICIO #############



# Ejercicio: Gestión de Inventario de una Tienda
# Descripción:
# Tu tarea es crear un programa para gestionar el inventario de una tienda. La tienda vende varios productos, y cada producto tiene un nombre, una categoría, una cantidad en stock y un precio por unidad. Los datos de los productos se almacenarán en un diccionario donde la clave es el nombre del producto y el valor es otro diccionario con la categoría, cantidad y precio.

# Requisitos:

# Crear una función para agregar un nuevo producto al inventario.
# Crear una función para actualizar la cantidad en stock de un producto existente.
# Crear una función para listar todos los productos de una categoría específica.
# Crear una función para calcular el valor total del inventario (cantidad en stock * precio por unidad).











############# EJERCICIO #############

# Escriba un programa que cree un diccionario que asocie como clave el nombre, y como valores ponga edad, dni, y direccion.
# Es decir debe ser otro diccionario dentro del diccionario con clave nombre.
# Inventelo, al menos introduzca 5 personas.
# Realice diferentes funciones que trabajen sobre este diccionario.
# ejemplo -> get_edad(diccionario, nombre) -> devuelve la edad de la persona.
# ejemplo -> get_dni(diccionario, nombre) -> devuelve el dni de la persona.
# ejemplo -> get_direccion(diccionario, nombre) -> devuelve la direccion de la persona.








############# EJERCICIO #############

# Leer el archivo logs.txt y crear un diccionario, que cada clave sea 0, 1, 2, etc y luego los valores que son:
# fecha, navegador, ip, codigo de respuesta del servidor (fecha, navegador, ip, server_respuesta)
# Imprimir el diccionario en pantalla.
# Una vez terminado intentar poner excepciones en caso de que el archivo no exista, o no se pueda abrir, etc.



# leer el archivo logs.txt

nombre_archivo = "logs.txt"

try:
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()
        diccionario = {}
        for i, linea in enumerate(lineas):
            datos = linea.split()
            fecha = datos[0]
            navegador = datos[1]
            ip = datos[2]
            server_respuesta = datos[3]
            diccionario[i] = {
                "fecha": fecha,
                "navegador": navegador,
                "ip": ip,
                "server_respuesta": server_respuesta
            }
        print(diccionario)
except FileNotFoundError:
    print(f"El archivo {nombre_archivo} no existe.")





    



############# EJERCICIO #############

# Explique con sus palabras la diferencia que existe entre una función y un método.
# Haga un código simple en donde se muestre la diferencia entre ambos.






############# EJERCICIO #############


Vamos a leer un archivo que obtenemos secretamente de los envíos de mensajes de la segunda guerra mundial.

el archivo se llama: mensajes_encriptados.txt

aquí vamos a encontrar caracteres alfanumericos y espacios, que es lo que se utilizaba para enviar mensajes encriptados.

Éste archivo debemos ordenarlo perfectamente para guardarlo en otros archivos y enviarlo a la maquina "Bombe" (diseñada por Turing) para que lo descifre.
Los archivo deben cumplir la siguiente logica:
    - Debemos separar todas las palabras por sus espacios, y luego dividirlas en cantidad de caracteres.
    - Cada cantidad diferente la vamos a guardar en un archivo diferente, por ejemplo:
        caracteres_1.txt
        caracteres_2.txt
        caracteres_3.txt
    - Y en cada archivo debemos guardar las palabras que tengan esa cantidad de caracteres. Pero manteniendo la siguiente logica:
        Debe en una línea mostrar la palabra, luego una coma, indicar nro de linea del archivo, coma y posicion dentro de la linea,
        ejemplo:
        jhdhjhd, 3, 20  -> esto es dicha palabra estaba en el archivo original en la línea 3, posicion 20
        j627hsj2jkj2, 5, 10 -> esto es dicha palabra estaba en el archivo original en la línea 5, posicion 10

        Estos archivos los debemos guardar dentro de un directorio llamado entrada_enigma/ y cada archivo

        


        


############# EJERCICIO #############


# Vamos a leer el archivo access.log y vamos a crear un diccionario con la siguiente estructura:
logs = {
    'linea-1': {
        'texto-completo': 'linea completa del archivo',
        'ip': 'ip acceso',  # (seleccionar los primeros 16 caracteres, eliminar doble comillas)
        'login': 'true/false',  # (true si está el string POST /wp-login.php que significa que hubo intento de login)
        'acceso-inseguro': 'true/false',  # (true si está el string xmlrpc.php que es un archivo que utilizan para intentar hackear / false si no está)
    },
    'linea-2': {
        'texto-completo': 'linea completa del archivo',
        'ip': 'ip acceso',  # (seleccionar los primeros 16 caracteres, eliminar doble comillas)
        'login': 'true/false',  # (true si está el string POST /wp-login.php que significa que hubo intento de login)
        'acceso-inseguro': 'true/false',  # (true si está el string xmlrpc.php que es un archivo que utilizan para intentar hackear / false si no está)
    },
}

# documentación de python métodos que pueden ser útiles:
# https://docs.python.org/3/library/stdtypes.html#str.find
# https://docs.python.org/3/library/stdtypes.html#str.replace


# Teniendo el diccionario, realizar una función que nos devuelva una lista de ips que intentaron hacer login
# Y otra función que nos devuelva una lista de ips que intentaron acceder a xmlrpc.php
# ejemplo:
# ips_login = get_ips_login(logs)
# ips_xmlrpc = get_ips_xmlrpc(logs)


# Luego de que funcione correctamente, intentar por un lado realizar tratamiento de errores.
# Y por otro lado, intentar codificarlo para que cumpla con las reglas de zen de python.








############# EJERCICIO #############




# En el siguiente código, deben agregar try y except para manejar posibles excepciones que puedan ocurrir en ambas funciones: dividir y leer_y_escribir_archivo.
# Deben asegurarse de gestionar errores comunes como la división por cero, entrada de valores no numéricos, archivos no encontrados y permisos de escritura."

"""


def dividir():
    """Divide dos números ingresados por el usuario y muestra el resultado."""
    num1 = input("Ingrese el primer número: ")
    num2 = input("Ingrese el segundo número: ")
    
    resultado = float(num1) / float(num2)

    print(f"El resultado de la división es: {resultado}")

def leer_y_escribir_archivo():
    """Lee el contenido de un archivo y escribe un nuevo contenido en el mismo archivo."""
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
        
    nuevo_contenido = input("Ingrese el contenido para escribir en el archivo: ")
    
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(nuevo_contenido)
        print("Nuevo contenido escrito en el archivo.")

dividir()
leer_y_escribir_archivo()



