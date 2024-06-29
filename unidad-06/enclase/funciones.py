



# funciones

                            ## key word arguments
def imprimir_detalle_persona( **kwargs ):
    if "nombre" in kwargs:
        print("Nombre: ", kwargs["nombre"])
    if "edad" in kwargs:
        print("Edad: ", kwargs["edad"])
    if "ciudad" in kwargs:
        print("Ciudad: ", kwargs["ciudad"])
    if "pais" in kwargs:
        print("Pais: ", kwargs["pais"])
    

nombre = "Juan"
edad = 30

# print("el nombre es: ", nombre, " y la edad es: ", edad)

print(f"el nombre es: {nombre} y la edad es: {edad}")


# imprimir_detalle_persona(pais="Argentina", nombre="Juan")












