



# -----------------
# Ejercicio 6
# -----------------



# En el siguiente código, deben agregar try y except para manejar posibles excepciones que puedan ocurrir en todas las funciones.
# Deben asegurarse de gestionar errores comunes como la división por cero, entrada de valores no numéricos, archivos no encontrados y permisos de escritura,
# en donde crean necesario agregar los bloques.

# Nota: No es necesario modificar el código existente, solo agregar los bloques try y except donde sea necesario. Y que siga funcionando pero ahora pudiendo trabajar con los errores

def dividir_numeros():
    """Divide dos números ingresados por el usuario y muestra el resultado."""
    numero1 = input("Ingrese el primer número: ")
    numero2 = input("Ingrese el segundo número: ")

    resultado = float(numero1) / float(numero2)
    print(f"El resultado de la división es: {resultado}")



def gestionar_archivo():
    """Lee el contenido de un archivo y escribe un nuevo contenido en el mismo archivo."""
    nombre_del_archivo = input("Ingrese el nombre del archivo: ")

    with open(nombre_del_archivo, 'r') as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)

    nuevo_contenido = input("Ingrese el nuevo contenido para escribir en el archivo: ")

    with open(nombre_del_archivo, 'w') as archivo:
        archivo.write(nuevo_contenido)
        print("Nuevo contenido escrito en el archivo.")



def calcular_promedio():
    """Calcula el promedio de una lista de números ingresados por el usuario."""
    numeros = input("Ingrese una lista de números separados por comas: ")
    lista_numeros = numeros.split(',')

    lista_numeros = [float(numero) for numero in lista_numeros]
    promedio = sum(lista_numeros) / len(lista_numeros)
    print(f"El promedio de los números ingresados es: {promedio}")



def contar_palabras():
    """Cuenta el número de palabras en una cadena de texto ingresada por el usuario."""
    texto = input("Ingrese un texto: ")
    palabras = texto.split()
    print(f"El número de palabras en el texto es: {len(palabras)}")



dividir_numeros()
gestionar_archivo()
calcular_promedio()
contar_palabras()

























# -----------------
# Ejercicio 6
# -----------------
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

