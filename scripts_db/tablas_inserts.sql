-- Inicia base de datos para catalogo de piezas

-- CLAVES
-- b_s, b_i,  h: Base superior, Base inferior, Alto
-- secciones: trapecios que forman a una pieza
-- cortes: Cantidad de cortes que hay entre patines y alma

-- Se usan tablas:
-- TABLES -> pieza ; trapecios ; valores
-- table pieza: id, familia, modelo de pieza
-- table parametros: informacion de cada pieza, cantidad de trapecios y cortes
-- table trapecios: (b_s, b_i, h) de cada seccion que forman una pieza

--  para mejor output en terminal sqlite
-- .mode table
-- .headers on

-- To export
-- .output results.txt
-- SELECT * FROM trapecios;
-- .output stdout


CREATE TABLE IF NOT EXISTS piezas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        familia TEXT NOT NULL,
        modelo TEXT NOT NULL UNIQUE
    )

CREATE TABLE IF NOT EXISTS parametros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo_seccion INTEGER NOT NULL,
        trapecios INTEGER NOT NULL,
        pieza_id INTEGER NOT NULL, 
        FOREIGN KEY (pieza_id) REFERENCES piezas (id)
    )

CREATE TABLE IF NOT EXISTS trapecios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo_seccion TEXT NOT NULL,
        posicion INTEGER NOT NULL,
        base_inf REAL NOT NULL,
        base_sup REAL NOT NULL,
        altura REAL NOT NULL,
        pieza_id INTEGER NOT NULL,
        FOREIGN KEY (pieza_id) REFERENCES piezas (id)
    )

-- Tablas no confirmadas para el schema.
CREATE TABLE IF NOT EXIST materiales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    peso REAL NOT NULL,
    -- equi_concreto REAL NOT NULL -- Equivalencia en concreto (Es mejor calcular en vez de guardar ??)
)

-- Nueva tabla TRAPECIOS seria:
CREATE TABLE IF NOT EXISTS trapecios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo_seccion TEXT NOT NULL,
        posicion INTEGER NOT NULL,
        base_inf REAL NOT NULL,
        base_sup REAL NOT NULL,
        altura REAL NOT NULL,
        pieza_id INTEGER NOT NULL,
        material_id INTEGER NOT NULL, -- Nueva relacion
        FOREIGN KEY (pieza_id) REFERENCES piezas (id),
        FOREIGN KEY (material_id) REFERENCES materiales (id) -- Nueva relacion
    )

CREATE TABLE IF NOT EXIST armaduras_activas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_id INTEGER NOT NULL,
    trapecio_id INTEGER NOT NULL,
    cota REAL NOT NULL, -- (Se guarda o define dinamicamente?) -- Coordenada vertical
    cantidad INT NOT NULL, -- numero de cordones por trapecio
    tipo TEXT NOT NULL, -- ejem T2, T4, T5 (Que tips de usan?) -- Pre-sets o sugerencias de posicines y cantidad de armaduras positivas
    area REAL NOT NULL, -- Area de cordon (Se guarda o calcula?)
    tpi REAL NOT NULL, -- se mide en [N/mm2] es resistencia de acero (Se guarda o calcula?) -- Usuario lo asigna, pero jacena recomienda por defecto 1400
    testero TEXT NOT NULL, -- que tipo de testero de usa (Preguntar Joaquin que tipos usan) -- Usan distintos tipos para distintas vigas/dallas
    FOREIGN KEY (material_id) REFERENCES materiales (id),
    FOREIGN KEY (trapecio_id) REFERENCES trapecios (id)
)

CREATE TABLE IF NOT EXIST armaduras_activas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_id INTEGER NOT NULL, -- No hace gran diferencia pero es bueno implementarlo de todas formas

    trapecio_id INTEGER NOT NULL,
    cota REAL NOT NULL, -- (Se guarda o define dinamicamente?) -- Coordenada vertical

    cantidad INT NOT NULL, -- numero de cordones por trapecio

    area REAL NOT NULL, -- Area de cordon (Se guarda o calcula?)

    testero TEXT NOT NULL, -- que tipo de testero de usa (Preguntar Joaquin que tipos usan) -- Usan distintos tipos para distintas vigas/dallas
    FOREIGN KEY (material_id) REFERENCES materiales (id),
    FOREIGN KEY (trapecio_id) REFERENCES trapecios (id)
)


-- tabla de DOCUMENTACION GENERAL 1. Armaduras Activas

-- NO SE PERMITE NUEVOS INSERTS A ESTA TABLA. 
-- ES UNA TABLA REFERENCIAL
CREATE TABLE IF NOT EXIST propiedades_armadura_activa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_comun TEXT,
    acero_completo TEXT,
    acero_corto TEXT,
    diametro REAL, -- FI  [mm]
    masa REAL, -- [Kg/m]
    area REAL, -- [cm2]
    carga_rotura REAL, -- [kN] KiloNewton
    limmite_elastico REAL -- [kN] KiloNewton
)

CREATE TABLE propiedades_armadura_activa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_comun TEXT,
    acero_completo TEXT,
    acero_corto TEXT,
    diametro REAL,
    masa REAL,
    area REAL,
    carga_rotura REAL,
    limmite_elastico REAL
);

-- reminder
-- para agregar:
-- INSERT INTO table_name (Col1, Col2) VALUES (Val1, Val2)
-- delete
-- DELETE FROM table WHERE condition;

-- valores de cotas para TESTERO 0.6 PULGADAS
[0.050, 0.110, 0.170, 0.230, 0.290, 
0.350, 0.410, 0.470, 
0.530, 0.590, 0.650, 
0.710, 0.770, 0.830, 0.890, 
0.950, 1.010, 1.070, 
1.130, 1.190, 1.250, 1.310]

CREATE TABLE IF NOT EXIST testero_06 (
    id INTEGER PRIMARY KEY,
    posicion INTEGER, -- posicion (index) desde abajo hacia arriba
    cota REAL, -- distancia en metros [m] desde base de pieza hasta centroide de cordon en esa posicion
)

-- Inserts de pos/cota de TESTERO 0.60 PULGADAS
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 1, 0.050);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 2, 0.110);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 3, 0.170);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 3, 0.230);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 4, 0.290);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 5, 0.350);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 6, 0.410);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 7, 0.470);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 8, 0.530);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 9, 0.590);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 10, 0.650);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 11, 0.710);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 12, 0.770);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 13, 0.830);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 14, 0.890);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 15, 0.950);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 16, 1.010);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 17, 1.070);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 18, 1.130);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 19, 1.190);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 20, 1.250);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.6''", 21, 1.310);



-- INSERTS PARA tabla de propiedades de armaduras activas:

INSERT INTO propiedades_armadura_activa (nombre_comun, acero_completo, acero_corto, diametro, masa, area, carga_rotura, limmite_elastico)
    VALUES ('Alambre 5mm', 'ASTM-421M Grado 1655 R2', 'ASTM-421M', 4.98, 0.153, 0.195, 32.2, 29);

INSERT INTO propiedades_armadura_activa (nombre_comun, acero_completo, acero_corto, diametro, masa, area, carga_rotura, limmite_elastico)
    VALUES ('Cordon 3/8''''', 'ASTM-416M Grado 1860 R2', 'ASTM-416M', 9.53, 0.432, 0.548, 102.3, 92.1);

INSERT INTO propiedades_armadura_activa (nombre_comun, acero_completo, acero_corto, diametro, masa, area, carga_rotura, limmite_elastico)
    VALUES ('Cordon 1/2''''', 'ASTM-416M Grado 1860 R2', 'ASTM-416M', 12.7, 0.775, 0.987, 183.7, 165.3);

INSERT INTO propiedades_armadura_activa (nombre_comun, acero_completo, acero_corto, diametro, masa, area, carga_rotura, limmite_elastico)
    VALUES ('Cordon 0.6''''', 'ASTM-416M Grado 1860 R2', 'ASTM-416M', 15.24, 1.102, 1.400, 260.7, 234.6);


-- Tabla para unidades de tahla armaduas activas y testeros.

CREATE TABLE unidades(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_medida TEXT,
    unidad TEXT
);

INSERT INTO unidades (nombre_medida, unidad) VALUES ('cota', 'metros [m]');
INSERT INTO unidades (nombre_medida, unidad) VALUES ('diametro', 'phi milimetros [mm]');
INSERT INTO unidades (nombre_medida, unidad) VALUES ('masa', 'kilogramos/metro [kg/m]');
INSERT INTO unidades (nombre_medida, unidad) VALUES ('area', 'centrimetros cuadrados [cm2]');
INSERT INTO unidades (nombre_medida, unidad) VALUES ('carga de rotura', 'Kilo Newton [kN]');
INSERT INTO unidades (nombre_medida, unidad) VALUES ('limite elastico', 'Kilo Newton [kN]');



-- RELACION TESTEROS
CREATE TABLE testeros (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    testero TEXT NOT NULL,
    posicion INTEGER UNIQUE NOT NULL, 
    cota REAL UNIQUE NOT NULL);