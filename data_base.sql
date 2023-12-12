CREATE DATABASE IF NOT EXISTS domiciliosRestaurante;

USE domiciliosRestaurante;

CREATE TABLE IF NOT EXISTS usuario (
    cliente_id varchar(10) PRIMARY KEY,
    nombre varchar(20) NOT NULL,
    correo varchar(50) NOT NULL UNIQUE,
    celular varchar(10) NOT NULL UNIQUE,
    ciudad varchar(20) NOT NULL,
    direccion varchar(80) NOT NULL,
    contrasena varchar(20) UNIQUE
);

CREATE TABLE IF NOT EXISTS cocinero (
    cocinero_id varchar(10) PRIMARY KEY,
    nombre varchar(20) NOT NULL,
    celular varchar(10) NOT NULL UNIQUE,
    edad int NOT NULL,
    anios_experiencia int NOT NULL
);

CREATE TABLE IF NOT EXISTS delivery (
    delivery_id varchar(10) PRIMARY KEY,
    nombre varchar(20) NOT NULL,
    celular varchar(10) NOT NULL UNIQUE,
    edad int NOT NULL,
    anios_experiencia int NOT NULL,
    tipo_de_lisencia varchar(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS plato (
    plato_id varchar(2) PRIMARY KEY,
    tipo_de_plato varchar(10) NOT NULL,
    tiempos FLOAT NOT NULL,
    nombre_plato varchar(50) NOT NULL,
    descripcion varchar(100) NOT NULL,
    precio FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS pedido (
    pedido_id varchar(10) PRIMARY KEY,
    plato_id varchar(10) NOT NULL,
    cocinero_id varchar(10) NOT NULL,
    cantidad int NOT NULL,
    precio_pedido FLOAT NOT NULL,
    FOREIGN KEY (plato_id) REFERENCES plato(id),
    FOREIGN KEY (cocinero_id) REFERENCES cocinero(id)
);

CREATE TABLE IF NOT EXISTS envio (
    envio_id varchar(6) PRIMARY KEY,
    pedido_id varchar(6) NOT NULL,
    cliente_id varchar(10) NOT NULL,
    delivery_id varchar(10) NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES cuenta(id),
    FOREIGN KEY (cliente_id) REFERENCES cliente(id),
    FOREIGN KEY (delivery_id) REFERENCES delivery(id)
);

-- cocinero
INSERT INTO cocinero VALUES ("01", "marco sanint", "001", 35, 12);

-- delivery
INSERT INTO delivery VALUES ("05", "mateo sanint", "005", 25, 6, "carro");

-- platos
INSERT INTO plato VALUES ('01', 'entrada', 10.0, 'Camarones apanados', '6 camarones apanados acompañados con salsa de la casa', 20000.0);
INSERT INTO plato VALUES ('02', 'entrada', 12.0, 'Ensalada César', 'Ensalada de lechuga romana, crutones, parmesano y aderezo especial', 18000.0);
INSERT INTO plato VALUES ('03', 'entrada', 8.0, 'Empanadas de queso', 'Empanadas rellenas de queso, acompañadas de salsa de tomate', 15000.0);
INSERT INTO plato VALUES ('04', 'entrada', 15.0, 'Tacos de camarón', 'Tacos de camarón con guacamole y salsa picante', 22000.0);

INSERT INTO plato VALUES ('05', 'plato fuerte', 20.0, 'Pasta carbonara', '500 g de pasta con salsa carbonara, queso azul y tocineta picada', 35000.0);
INSERT INTO plato VALUES ('06', 'plato fuerte', 22.0, 'Lomo a la pimienta', 'Filete de lomo bañado en salsa de pimienta, acompañado de papas', 38000.0);
INSERT INTO plato VALUES ('07', 'plato fuerte', 18.0, 'Pollo al curry', 'Pollo en salsa de curry con arroz y verduras', 32000.0);
INSERT INTO plato VALUES ('08', 'plato fuerte', 25.0, 'Salmón a la plancha', 'Salmón grillado con limón, acompañado de puré de papas', 42000.0);

INSERT INTO plato VALUES ('09', 'jugo', 5.0, 'Jugo de mango', '350 ml de jugo natural de mango con base en leche', 10000.0);
INSERT INTO plato VALUES ('10', 'jugo', 6.0, 'Limonada refrescante', 'Limonada natural con hojas de menta y hielo', 8000.0);
INSERT INTO plato VALUES ('11', 'jugo', 7.0, 'Fresa Colada', 'Batido de fresas con coco y leche', 12000.0);
INSERT INTO plato VALUES ('12', 'jugo', 4.0, 'Jugo de piña', '250 ml de jugo natural de piña', 9000.0);

INSERT INTO plato VALUES ('13', 'postre', 15.0, 'Torta con helado', 'Una buena porción de torta de chocolate con helado', 20000.0);
INSERT INTO plato VALUES ('14', 'postre', 18.0, 'Helado de vainilla con frutas', 'Tazón de helado de vainilla con fresas y kiwi', 16000.0);
INSERT INTO plato VALUES ('15', 'postre', 12.0, 'Mousse de chocolate', 'Deliciosa mousse de chocolate con crema batida', 18000.0);
INSERT INTO plato VALUES ('16', 'postre', 20.0, 'Cheesecake de frutos rojos', 'Porción de cheesecake con salsa de frutos rojos', 22000.0);

INSERT INTO pedido VALUES (pedido_id varchar(10) PRIMARY KEY,
    plato_id varchar(10) NOT NULL,
    cocinero_id varchar(10) NOT NULL,
    cantidad int NOT NULL,
    precio_pedido FLOAT NOT NULL)