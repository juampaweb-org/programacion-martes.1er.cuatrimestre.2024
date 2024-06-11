

# -----------------
# Ejercicio 10
# -----------------



# En el siguiente código, deben agregar try y except para manejar posibles excepciones que puedan ocurrir en ambas funciones: dividir y leer_y_escribir_archivo.
# Deben asegurarse de gestionar errores comunes como la división por cero, entrada de valores no numéricos, archivos no encontrados y permisos de escritura."


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



