CREATE DATABASE grafos;
use grafos;

-- Tabla de ciudades
create table ciudades (
ciu_id INT AUTO_INCREMENT PRIMARY KEY,
ciu_nombre VARCHAR(80) NOT NULL
);

-- Tabla de conexión
create table conexiones (
    cone_id INT AUTO_INCREMENT PRIMARY KEY,  
    ciu1_id INT,
    ciu2_id INT,
    ciu1_nombre VARCHAR(80),
    ciu2_nombre VARCHAR(80),
    FOREIGN KEY (ciu1_id) REFERENCES ciudades(ciu_id),
    FOREIGN KEY (ciu2_id) REFERENCES ciudades(ciu_id),
    UNIQUE (ciu1_id, ciu2_id)   
);


-- Procedimientos de almacenamiento
delimiter //
CREATE PROCEDURE crear_conexion(IN ciu1_nombre VARCHAR(80), IN ciu2_nombre VARCHAR(80))
BEGIN
DECLARE ciu1_id INT;
DECLARE ciu2_id INT;

-- Obtener los IDs de las ciudades a partir de sus nombres
SELECT ciu_id INTO ciu1_id FROM ciudades WHERE ciu_nombre = ciu1_nombre;
SELECT ciu_id INTO ciu2_id FROM ciudades WHERE ciu_nombre = ciu2_nombre;

-- Verificar si los IDs son válidos
IF ciu1_id IS NOT NULL AND ciu2_id IS NOT NULL THEN
-- Insertar la conexión en la tabla de conexiones, guardando también los nombres
INSERT IGNORE INTO conexiones (ciu1_id, ciu2_id, ciu1_nombre, ciu2_nombre)
VALUES (ciu1_id, ciu2_id, ciu1_nombre, ciu2_nombre);
END IF;
END //
delimiter ;

delimiter //
CREATE PROCEDURE crear_ciudad(IN ciu_nombre VARCHAR(80))
BEGIN
INSERT IGNORE INTO ciudades (ciu_nombre)
VALUES (ciu_nombre);
END //
delimiter ;

-- Crear ciudades
CALL crear_ciudad('Chinchina');
CALL crear_ciudad('Manizales');
CALL crear_ciudad('Pereira');
CALL crear_ciudad('Villamaria');
CALL crear_ciudad('Palestina');
CALL crear_ciudad('Neira');
CALL crear_ciudad('La virginia');
CALL crear_ciudad('Dosquebradas');
CALL crear_ciudad('Santa Rosa de Cabal');
CALL crear_ciudad('Cartago');
CALL crear_ciudad('Calarca');
CALL crear_ciudad('Ciscasia');
CALL crear_ciudad('La tebaida');
CALL crear_ciudad('Montenegro');
CALL crear_ciudad('Armenia');


-- Crear conexión entre las ciudades
CALL crear_conexion('Manizales', 'Pereira');
CALL crear_conexion('Manizales', 'Armenia');
CALL crear_conexion('Manizales', 'Chinchina');
CALL crear_conexion('Manizales', 'Villamaria');
CALL crear_conexion('Manizales', 'Palestina');
CALL crear_conexion('Manizales', 'Neira');
CALL crear_conexion('Manizales', 'La virginia');
CALL crear_conexion('Manizales', 'Dosquebradas');
CALL crear_conexion('Manizales', 'Santa Rosa de Cabal');
CALL crear_conexion('Manizales', 'Cartago');

CALL crear_conexion('Pereira', 'Manizales');
CALL crear_conexion('Pereira', 'Dosquebradas');
CALL crear_conexion('Pereira', 'Cartago');
CALL crear_conexion('Pereira', 'Ciscasia');
CALL crear_conexion('Pereira', 'La virginia');

CALL crear_conexion('Armenia', 'Manizales');
CALL crear_conexion('Armenia', 'Pereira');
CALL crear_conexion('Armenia', 'Santa Rosa de Cabal');
CALL crear_conexion('Armenia', 'Cartago');
CALL crear_conexion('Armenia', 'Calarca');
CALL crear_conexion('Armenia', 'La tebaida');
CALL crear_conexion('Armenia', 'Montenegro');
CALL crear_conexion('Armenia', 'Ciscacia');
CALL crear_conexion('Armenia', 'Dosquebradas');

CALL crear_conexion('Chinchina', 'Manizales');

CALL crear_conexion('Villamaria', 'Manizales');

CALL crear_conexion('Palestina', 'Manizales');

CALL crear_conexion('Neira', 'Manizales');

CALL crear_conexion('La virginia', 'Cartago');
CALL crear_conexion('La virginia', 'Pereira');

CALL crear_conexion('Dosquebradas', 'Manizales');
CALL crear_conexion('Dosquebradas', 'Pereira');
CALL crear_conexion('Dosquebradas', 'Cartago');
CALL crear_conexion('Dosquebradas', 'Armenia');

CALL crear_conexion('Santa Rosa de Cabal', 'Manizales');
CALL crear_conexion('Santa Rosa de Cabal', 'Pereira');
CALL crear_conexion('Santa Rosa de Cabal', 'Armenia');

CALL crear_conexion('Cartago', 'La virginia');
CALL crear_conexion('Cartago', 'Manizales');
CALL crear_conexion('Cartago', 'Pereira');
CALL crear_conexion('Cartago', 'Dosquebradas');
CALL crear_conexion('Cartago', 'Armenia');

CALL crear_conexion('Calarca', 'Armenia');

CALL crear_conexion('Ciscasia', 'Armenia');

CALL crear_conexion('La tebaida', 'Armenia');

CALL crear_conexion('Montenegro', 'Armenia');

-- Consultar conexiones
SELECT cone_id, ciu1_nombre, ciu2_nombre, ciu1_id, ciu2_id FROM conexiones;

DELIMITER //
CREATE PROCEDURE leer_conexion(IN ciu_nombre VARCHAR(80))
BEGIN
    SELECT ciu1_nombre, ciu2_nombre
    FROM conexiones
    WHERE ciu1_nombre = ciu_nombre
       OR ciu2_nombre = ciu_nombre;
END //
DELIMITER ;

call leer_conexion ('Manizales');

DELIMITER //
CREATE PROCEDURE actualizar_conexion(IN ciu_id INT, IN ciu1_nueva VARCHAR(80),IN ciu2_nueva VARCHAR(80))
BEGIN
IF ciu1_nueva IS NOT NULL THEN
UPDATE conexiones
SET ciu1_nombre = ciu1_nueva
WHERE cone_id = ciu_id;
END IF;
IF ciu2_nueva IS NOT NULL THEN
UPDATE conexiones
SET ciu2_nombre = ciu2_nueva
WHERE cone_id = ciu_id;
END IF;
END //
DELIMITER ;

CALL actualizar_conexion(46, 'Circasia', 'Dosquebradas');

DROP PROCEDURE IF EXISTS actualizar_conexion;


DELIMITER //
CREATE PROCEDURE eliminar_conexion(IN ciudad1_nombre VARCHAR(80), IN ciudad2_nombre VARCHAR(80))
BEGIN
    DELETE FROM conexiones 
    WHERE (ciu1_nombre = ciudad1_nombre AND ciu2_nombre = ciudad2_nombre)
       OR (ciu1_nombre = ciudad2_nombre AND ciu2_nombre = ciudad1_nombre);
END //
DELIMITER ;

CALL eliminar_conexion('Manizales','Pereira');
DROP PROCEDURE IF EXISTS eliminar_conexion;
