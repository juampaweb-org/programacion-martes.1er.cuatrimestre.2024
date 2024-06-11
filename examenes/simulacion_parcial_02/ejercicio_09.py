# -----------------
# Ejercicio 9
# -----------------

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
