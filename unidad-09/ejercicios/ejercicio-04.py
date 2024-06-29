# 4. Recorrer un diccionario:
# Usa el diccionario contactos.
# Recorre todas las claves del diccionario y las imprime.
# Recorre todos los valores del diccionario y los imprime.
# Recorre todos los pares clave-valor y los imprime.


diccionario = {}


def imprimir_diccionario( mi_diccionario ):
    """
    Va a imprimir el diccionario que recibe como argumento
    args:
        mi_diccionario: dict
    """
    print(mi_diccionario)
    return True



# este es mi script
diccionario_agenda = {
    "pepe":"1145679853",
    "jose":"1175644563",
    "carlos":"1189745613",
    }


imprimir_diccionario( diccionario_agenda )
