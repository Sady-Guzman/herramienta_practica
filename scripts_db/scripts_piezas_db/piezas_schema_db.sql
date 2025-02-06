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




-- sqlite> .schema
CREATE TABLE piezas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        familia TEXT NOT NULL,
        modelo TEXT NOT NULL
    );
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE parametros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo_seccion INTEGER NOT NULL,
        trapecios INTEGER NOT NULL,
        pieza_id INTEGER NOT NULL, 
        FOREIGN KEY (pieza_id) REFERENCES piezas (id)
    );
CREATE TABLE trapecios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo_seccion TEXT NOT NULL,
        posicion INTEGER NOT NULL,
        base_inf REAL NOT NULL,
        base_sup REAL NOT NULL,
        altura REAL NOT NULL,
        pieza_id INTEGER NOT NULL,
        FOREIGN KEY (pieza_id) REFERENCES piezas (id)
    );
-- .exit

-- TABLA NO CONFIRMADA
-- Deberia crearse en otro .db


-- Tablas no confirmadas para el schema.
CREATE TABLE IF NOT EXIST materiales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    peso REAL NOT NULL,
    -- equi_concreto REAL NOT NULL -- Equivalencia en concreto (Es mejor calcular en vez de guardar ??)
)

-- INSERTS PARA TABLAS DE PIEZAS EN CATALOGO.DB se guardan en su propia carpeta. Un archivo de insert por cada pieza