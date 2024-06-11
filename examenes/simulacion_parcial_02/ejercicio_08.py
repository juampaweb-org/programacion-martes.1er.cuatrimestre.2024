"""

# -----------------
# Ejercicio 8
# -----------------

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

        



"""