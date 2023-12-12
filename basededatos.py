import sqlite3
from datetime import datetime

connection = sqlite3.connect("domiciliosRestaurante.db")
cursor = connection.cursor()

# Crear tabla de usuario
cursor.execute(f"CREATE TABLE IF NOT EXISTS usuario (cliente_id varchar(10) PRIMARY KEY, nombre varchar(20) NOT NULL, correo varchar(50) NOT NULL UNIQUE, celular varchar(10) NOT NULL UNIQUE, ciudad varchar(20) NOT NULL, direccion varchar(80) NOT NULL, contrasena varchar(20) UNIQUE)")

# Crear la tabla de cocinero
cursor.execute(f"CREATE TABLE IF NOT EXISTS cocinero (nombre varchar(20) NOT NULL, celular varchar(10) NOT NULL UNIQUE, edad int NOT NULL, anios_experiencia int NOT NULL)")

# Crear la tabla de delivery
cursor.execute(f"CREATE TABLE IF NOT EXISTS delivery (delivery_id varchar(10) PRIMARY KEY, nombre varchar(20) NOT NULL, celular varchar(10) NOT NULL UNIQUE, edad int NOT NULL, anios_experiencia int NOT NULL, tipo_de_lisencia varchar(10) NOT NULL)")

# Crear la tabla de plato 
cursor.execute(f"CREATE TABLE IF NOT EXISTS plato (plato_id varchar(2) PRIMARY KEY, tipo_de_plato varchar(10) NOT NULL, tiempos FLOAT NOT NULL, nombre_plato varchar(20) NOT NULL, descripcion varchar(100) NOT NULL, precio FLOAT NOT NULL)")

# Crear la tabla de pedido
cursor.execute(f"CREATE TABLE IF NOT EXISTS pedido (pedido_id varchar(10) PRIMARY KEY, plato_id varchar(10) NOT NULL, cocinero_id varchar(10) NOT NULL, cantidad int NOT NULL, precio_pedido FLOAT NOT NULL, FOREIGN KEY (plato_id) REFERENCES plato(id), FOREIGN KEY (cocinero_id) REFERENCES cocinero(id))")

# Crear la tabla de envio
cursor.execute(f"CREATE TABLE IF NOT EXISTS envio (envio_id varchar(6) PRIMARY KEY, pedido_id varchar(6) NOT NULL, cliente_id varchar(10) NOT NULL, delivery_id varchar(10) NOT NULL, FOREIGN KEY (pedido_id) REFERENCES cuenta(id), FOREIGN KEY (cliente_id) REFERENCES cliente(id), FOREIGN KEY (delivery_id) REFERENCES delivery(id))")

# Crear platos
cursor.execute(f"INSERT INTO plato VALUES ('01', 'entrada', 10.0, 'Camarones apanados', '6 camarones apanados acompañados con salsa de la casa', 20000.0);")
cursor.execute(f"INSERT INTO plato VALUES ('02', 'entrada', 12.0, 'Ensalada César', 'Ensalada de lechuga romana, crutones, parmesano y aderezo especial', 18000.0);")
cursor.execute(f"INSERT INTO plato VALUES ('03', 'entrada', 8.0, 'Empanadas de queso', 'Empanadas rellenas de queso, acompañadas de salsa de tomate', 15000.0);")
cursor.execute(f"INSERT INTO plato VALUES ('04', 'entrada', 15.0, 'Tacos de camarón', 'Tacos de camarón con guacamole y salsa picante', 22000.0);")

cursor.execute(f"INSERT INTO plato VALUES ('05', 'plato fuerte', 20.0, 'Pasta carbonara', '500 g de pasta con salsa carbonara, queso azul y tocineta picada', 35000.0);")
cursor.execute(f"INSERT INTO plato VALUES ('06', 'plato fuerte', 22.0, 'Lomo a la pimienta', 'Filete de lomo bañado en salsa de pimienta, acompañado de papas', 38000.0);")
cursor.execute(f"INSERT INTO plato VALUES ('07', 'plato fuerte', 18.0, 'Pollo al curry', 'Pollo en salsa de curry con arroz y verduras', 32000.0);")
cursor.execute(f"INSERT INTO plato VALUES ('08', 'plato fuerte', 25.0, 'Salmón a la plancha', 'Salmón grillado con limón, acompañado de puré de papas', 42000.0);")

cursor.execute(f"INSERT INTO plato VALUES ('09', 'jugo', 5.0, 'Jugo de mango', '350 ml de jugo natural de mango con base en leche', 10000.0);")
cursor.execute(f"INSERT INTO plato VALUES ('10', 'jugo', 6.0, 'Limonada refrescante', 'Limonada natural con hojas de menta y hielo', 8000.0);")
cursor.execute(f"INSERT INTO plato VALUES ('11', 'jugo', 7.0, 'Fresa Colada', 'Batido de fresas con coco y leche', 12000.0);")
cursor.execute(f"INSERT INTO plato VALUES ('12', 'jugo', 4.0, 'Jugo de piña', '250 ml de jugo natural de piña', 9000.0);")

cursor.execute(f"INSERT INTO plato VALUES ('13', 'postre', 15.0, 'Torta con helado', 'Una buena porción de torta de chocolate con helado', 20000.0);")
cursor.execute(f"INSERT INTO plato VALUES ('14', 'postre', 18.0, 'Helado de vainilla con frutas', 'Tazón de helado de vainilla con fresas y kiwi', 16000.0);")
cursor.execute(f"INSERT INTO plato VALUES ('15', 'postre', 12.0, 'Mousse de chocolate', 'Deliciosa mousse de chocolate con crema batida', 18000.0);")
cursor.execute(f"INSERT INTO plato VALUES ('16', 'postre', 20.0, 'Cheesecake de frutos rojos', 'Porción de cheesecake con salsa de frutos rojos', 22000.0);")


# agregar datos de usuarios
def add_data(table_name, columns, values):
    column_names = ", ".join(columns)
    placeholders = ", ".join(["?"] * len(columns))
    cursor.execute(f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})", tuple(values))
    connection.commit()
    print(f"Data added to {table_name} successfully.")

#agregar facturas
def crear_pedido(plato_id, cantidad, precio_total):
    cursor.execute("INSERT INTO factura (pedido_id, producto_id, total) VALUES (1, ?, 01, ?, ?)", (plato_id, cantidad, precio_total))
    connection.commit()
    print("Pedido realizado.")

#____________________________________________________________________________________________________________#
#Selects

# sacar todo el menu (los platos)
def get_menu():
    cursor.execute("SELECT plato_id, tipo_de_plato, nombre_plato, precio FROM plato")
    return cursor.fetchall()

# selecciona la contraseña del usuario
def get_password(gmail):
    cursor.execute("SELECT contrasena FROM usuario WHERE correo = ?", (gmail,))
    return cursor.fetchone()

# descripcion del plato por el id
def descripcion(id):
    cursor.execute("SELECT descripcion FROM plato WHERE plato_id = ?", (id,))
    return cursor.fetchone()

# Close the connection to the database
def close():
    cursor.close()
    connection.close()
