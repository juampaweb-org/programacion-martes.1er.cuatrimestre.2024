

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

