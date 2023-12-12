#en el archivo menu.py hay esto:
import assistant
import basededatos
from prettytable import PrettyTable

def convertir_numeros_letras_a_numeros(cadena):
    numeros_letras = {
        'cero': '0',
        'uno': '1',
        'dos': '2',
        'tres': '3',
        'cuatro': '4',
        'cinco': '5',
        'seis': '6',
        'siete': '7',
        'ocho': '8',
        'nueve': '9',
        'punto': '.',
        'arroba': '@'
    }

    palabras = cadena.lower().split()
    numeros = [numeros_letras[palabra] if palabra in numeros_letras else palabra for palabra in palabras]
    return ''.join(numeros)

# menu principal
def start():
    
    while True:
        realizar_pedidos()
        assistant.speak("Bienvenido al restaurante Carne en casa, este es el servicio a domicilio, ¿ya tienes una cuenta creada?, di si o no")
        command = assistant.listen().lower()

        print(command)
        if "no" in command:
            add_usuario()

        elif "sí" or "si" in command:
            log_in()

        elif "salir" in command:
            assistant.speak("Hasta luego")
            break

        else:
            assistant.speak("Lo siento, no entendí. Por favor, intenta de nuevo.")

# agregar usuario
def add_usuario():
    assistant.speak("Vamos a crearte una cuenta. Dime")
    assistant.speak("tu numero de documento")
    client_id = assistant.listen()
    client_id = convertir_numeros_letras_a_numeros(client_id)
    print(client_id)

    assistant.speak("tu nombre completo")
    client_name = assistant.listen()
    client_name = convertir_numeros_letras_a_numeros(client_name)
    print(client_name)

    assistant.speak("tu correo electronico")
    client_gmail = assistant.listen()
    client_gmail = convertir_numeros_letras_a_numeros(client_gmail)
    print(client_gmail)

    assistant.speak("tu numero de telefono")
    client_number = assistant.listen()
    client_number = convertir_numeros_letras_a_numeros(client_number)
    print(client_number)

    assistant.speak("tu ciudad")
    client_city = assistant.listen()
    client_city = convertir_numeros_letras_a_numeros(client_city)
    print(client_city)

    assistant.speak("tu direccion")
    client_direction = assistant.listen()
    client_direction = convertir_numeros_letras_a_numeros(client_direction)
    print(client_direction)
    
    assistant.speak("y finalmente, ¿cual seria la contraseña?")
    client_password = assistant.listen()
    client_password = convertir_numeros_letras_a_numeros(client_password)
    print(client_password)

    basededatos.add_data("usuario", ["cliente_id", "nombre", "correo", "celular", "ciudad", "direccion", "contrasena"], [client_id, client_name, client_gmail, client_number, client_city, client_direction, client_password])

    assistant.speak("Cliente agregado exitosamente.")

# confirmar cuenta
def log_in():
    assistant.speak("Ingresa tu correo por favor")
    user_gmail = assistant.listen()
    user_gmail = convertir_numeros_letras_a_numeros(user_gmail)
    print(user_gmail)
    if user_gmail == "salir":
        start()

    assistant.speak("ahora tu contraseña")
    user_password = assistant.listen()
    user_password = convertir_numeros_letras_a_numeros(user_password)
    print(user_password)
    if user_password == "salir":
        start()

    password = check_user(user_gmail)
    print(password)
    if user_password in password:
        realizar_pedidos()
    else:
        assistant.speak("correo o contraseña incorrecta, intenta otra vez")
        log_in()


# muesta el menu para hacer pedidos
def realizar_pedidos():
    assistant.speak("Bienvenido, aquí tienes todo nuestro menú:")
    carta = imprimir_tabla_platos()
    print(carta)
    assistant.speak("¿Desea pedir?")
    pedido = assistant.listen()
    print(pedido)

    if pedido == "":
        realizar_pedidos()
    if "pregunta" in pedido:
        assistant.speak("¿Claro, dime?")
        plato_id = input()
        descripcion = descripcion_plato(plato_id)
        assistant.speak("El plato" + plato_id + " es " + descripcion)

#_______________________________________________________________________
# confirmar usuario
def check_user(gmail):
    res = basededatos.get_password(gmail)
    return res

# imprimir tablas
def imprimir_tabla_platos():
    menu = basededatos.get_menu()

    tabla = PrettyTable()
    tabla.field_names = ["plato_id", "Tipo de Plato", "Nombre del Plato", "Precio"]

    for plato in menu:
        tabla.add_row(plato)

    return str(tabla)

#devuelve la descripcion de un plato
def descripcion_plato(plato_id):
    des = basededatos.descripcion(plato_id)
    return str(des)