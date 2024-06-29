
# -----------
# Ejercicio 2
# -----------
# Utilizando el modulo os haga lo siguiente:
# Liste por pantalla todos los directorios y archivos de un directorio definido.


import os

# directorio definido
directorio = "."

# listar directorios y archivos
for elemento in os.listdir(directorio):
    print(elemento)