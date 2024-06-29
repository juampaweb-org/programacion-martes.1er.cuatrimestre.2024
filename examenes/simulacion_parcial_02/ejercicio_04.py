

# ------------------
# Ejercicio 4
# ------------------


# Ejercicio: Gestión de Inventario de una Tienda
# Descripción:
# Tu tarea es crear un programa para gestionar el inventario de una tienda. La tienda vende varios productos, y cada producto tiene un nombre, una categoría, una cantidad en stock y un precio por unidad. Los datos de los productos se almacenarán en un diccionario donde la clave es el nombre del producto y el valor es otro diccionario con la categoría, cantidad y precio.

# Requisitos:

# Crear una función para agregar un nuevo producto al inventario.
# Crear una función para actualizar la cantidad en stock de un producto existente.
# Crear una función para listar todos los productos de una categoría específica.
# Crear una función para calcular el valor total del inventario (cantidad en stock * precio por unidad).

productos = {
            'hamburguesas': {
                'categoria': 'comida',
                'cantidad': 100,
                'precio': 5.0
            },
            'papas_fritas': {
                'categoria': 'comida',
                'cantidad': 50,
                'precio': 2.5
            },
        }


# Agregar un nuevo producto al inventario
def agregar_producto(nombre, categoria, cantidad, precio):
    """
    Agrega un nuevo producto al inventario.
    Parametros:
        nombre (str): El nombre del producto.
        categoria (str): La categoria del producto.
        cantidad (int): La cantidad de producto en stock.
        precio (float): El precio por unidad del producto.
    """
    productos[nombre] = {
        'categoria': categoria,
        'cantidad': cantidad,
        'precio': precio
    }

    return productos

productos = agregar_producto('refresco', 'bebida', 200, 1.5)

print(productos)