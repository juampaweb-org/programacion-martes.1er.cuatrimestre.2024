

# Diferentes tipos de errores

# SyntaxError Errores de sintaxis



# Errores en tiempo de ejecución

# numero_uno = int(input("Ingrese un número: "))
# numero_dos = int(input("Ingrese otro número: "))




# Las palabras reservadas que nos ofrece Python para identificar errores son:
# try y except




try:
    numero = float(input("Ingrese un número natural: "))
    print("El reciproco de", numero, "es", 1 / numero)

except ZeroDivisionError:
    print("Error! No se puede dividir por cero.")

except:
    print("Error! Debe ingresar un número.")

except:
    print("Error generico...")


print("continua ejecutando el programa...")





