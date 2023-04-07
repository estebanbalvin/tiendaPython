# Definir una clase para representar una laptop
class Laptop:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

# Crear una lista de laptops disponibles en la tienda
laptops = [
    Laptop('HP', 'Pavilion', 800),
    Laptop('Lenovo', 'IdeaPad', 1200),
    Laptop('Dell', 'Inspiron', 1000)
]

# Función para mostrar las laptops disponibles
def mostrar_laptops():
    print('Laptops disponibles:')
    for i, laptop in enumerate(laptops):
        print(f'{i+1}. {laptop.marca} {laptop.modelo} - {laptop.precio}€')

# Función para añadir una laptop al carrito
def agregar_al_carrito():
    # Pedir al usuario que seleccione una laptop
    mostrar_laptops()
    laptop_seleccionada = int(input('Seleccione una laptop (1-3): ')) - 1
    laptop = laptops[laptop_seleccionada]

    # Pedir al usuario que indique la cantidad de laptops que desea
    cantidad = int(input('¿Cuántas laptops desea comprar?: '))

    # Añadir la laptop al carrito
    carrito.append((laptop, cantidad))
    print(f'Se han añadido {cantidad} {laptop.marca} {laptop.modelo} al carrito.')

# Función para mostrar el contenido del carrito y el precio total
def mostrar_carrito():
    if len(carrito) == 0:
        print('El carrito está vacío.')
    else:
        print('Contenido del carrito:')
        for laptop, cantidad in carrito:
            subtotal = laptop.precio * cantidad
            print(f'{cantidad} {laptop.marca} {laptop.modelo} - {subtotal}€')
        total = sum(laptop.precio * cantidad for laptop, cantidad in carrito)
        print(f'Total: {total}€')

# Función para realizar el pago y vaciar el carrito
def pagar():
    if len(carrito) == 0:
        print('No hay nada que pagar.')
    else:
        mostrar_carrito()
        confirmacion = input('¿Desea continuar con el pago? (s/n): ')
        if confirmacion == 's':
            total = sum(laptop.precio * cantidad for laptop, cantidad in carrito)
            print(f'Se ha realizado un pago de {total}€. ¡Gracias por su compra!')
            carrito.clear()

# Inicializar el carrito vacío
carrito = []

# Pedir al usuario que seleccione una acción
while True:
    print('¿Qué desea hacer?')
    print('1. Ver laptops disponibles')
    print('2. Añadir laptop al carrito')
    print('3. Ver contenido del carrito')
    print('4. Pagar')
    print('5. Salir')
    opcion = input('Seleccione una opción (1-5): ')

    if opcion == '1':
        mostrar_laptops()
    elif opcion == '2':
        agregar_al_carrito()
    elif opcion == '3':
        mostrar_carrito()
    elif opcion == '4':
        pagar()
    elif opcion == '5':
        break
    else:
        print('Opción no válida. Intente de nuevo.')
class Laptop:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

laptops_disponibles = [Laptop("Lenovo", "ThinkPad X1 Carbon", 1299.99),
                       Laptop("Dell", "XPS 13", 1099.99),
                       Laptop("HP", "Spectre x360", 1399.99),
                       Laptop("Apple", "MacBook Air", 999.99)]

carrito = {}

def mostrar_laptops():
    print("Laptops disponibles:")
    for i, laptop in enumerate(laptops_disponibles):
        print(f"{i+1}. {laptop.marca} {laptop.modelo} - ${laptop.precio}")
    print()

def agregar_al_carrito():
    mostrar_laptops()
    laptop_seleccionada = int(input("Seleccione una laptop para añadir al carrito: "))
    cantidad = int(input("Ingrese la cantidad que desea comprar: "))
    laptop = laptops_disponibles[laptop_seleccionada - 1]
    if laptop in carrito:
        carrito[laptop] += cantidad
    else:
        carrito[laptop] = cantidad
    print(f"{cantidad} {laptop.marca} {laptop.modelo} añadida(s) al carrito.\n")

def mostrar_carrito():
    total = 0
    if len(carrito) == 0:
        print("El carrito está vacío.\n")
    else:
        print("Contenido del carrito:")
        for laptop, cantidad in carrito.items():
            subtotal = laptop.precio * cantidad
            total += subtotal
            print(f"{cantidad} {laptop.marca} {laptop.modelo} - ${subtotal:.2f}")
        print(f"Total: ${total:.2f}\n")

def pagar():
    mostrar_carrito()
    if len(carrito) == 0:
        print("El carrito está vacío. No se puede realizar el pago.\n")
    else:
        confirmacion = input(f"Total a pagar: ${total:.2f}. ¿Desea confirmar la compra? (s/n)")
        if confirmacion.lower() == "s":
            print("Pago realizado con éxito. Gracias por su compra.\n")
            carrito.clear()
        else:
            print("Pago cancelado.\n")

while True:
    print("Bienvenido a la tienda de laptops online.")
    print("Seleccione una opción:")
    print("1. Ver laptops disponibles")
    print("2. Añadir al carrito")
    print("3. Ver carrito")
    print("4. Pagar")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        mostrar_laptops()
    elif opcion == 2:
        agregar_al_carrito()
    elif opcion == 3:
        mostrar_carrito()
    elif opcion == 4:
        pagar()
    elif opcion == 5:
        print("Gracias por visitar nuestra tienda en línea. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.\n")
