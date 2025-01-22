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
    cota REAL NOT NULL, -- (Se guarda o define dinamicamente?)
    cantidad INT NOT NULL, -- numero de cordones
    tipo TEXT NOT NULL, -- ejem T2, T4, T5 (Que tips de usan?)
    area REAL NOT NULL, -- Area de cordon (Se guarda o calcula?)
    tpi REAL NOT NULL, -- se mide en [N/mm2] es resistencia de acero (Se guarda o calcula?)
    testeto TEXT NOT NULL, -- que tipo de testero de usa (Preguntar Joaquin que tipos usan)
    FOREIGN KEY (material_id) REFERENCES materiales (id),
    FOREIGN KEY (trapecio_id) REFERENCES trapecios (id)
)



-- reminder
-- para agregar:
-- INSERT INTO table_name (Col1, Col2) VALUES (Val1, Val2)
-- delete
-- DELETE FROM table WHERE condition;
