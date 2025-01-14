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



CREATE TABLE IF NOT EXISTS piezas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        familia TEXT NOT NULL,
        modelo TEXT NOT NULL
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


-- para agregar:
-- INSERT INTO table_name (Col1, Col2) VALUES (Val1, Val2)
-- delete
-- DELETE FROM table WHERE condition;
-- !!!! Piezas de relleno para probar comboBox
-- INSERT INTO piezas (familia, modelo) VALUES ('VS', '4020');
-- INSERT INTO piezas (familia, modelo) VALUES ('VS', '4025');
-- INSERT INTO piezas (familia, modelo) VALUES ('VS', '4027');
-- INSERT INTO piezas (familia, modelo) VALUES ('VR', '1000');
-- INSERT INTO piezas (familia, modelo) VALUES ('VR', '1001');


-- -- >>> Piezas para catalogo con datos de JACENA
-- INSERT INTO piezas (familia, modelo) VALUES ('JI', '4060_CH');
-- INSERT INTO parametros (tipo_seccion, trapecios, pieza_id) VALUES (1, 1, 1)
-- INSERT INTO parametros (tipo_seccion, trapecios, pieza_id) VALUES (2, 5, 1)
-- -- 0.400 OR 0.4
-- INSERT INTO trapecios (tipo_seccion, posicion, base_inf, base_sup, altura, pieza_id) VALUES (1, 1, 0.400, 0.400, 0.600, 1)
-- INSERT INTO trapecios (tipo_seccion, posicion, base_inf, base_sup, altura, pieza_id) VALUES (2, 1, 0.400, 0.400, 0.080, 1)
-- INSERT INTO trapecios (tipo_seccion, posicion, base_inf, base_sup, altura, pieza_id) VALUES (2, 2, 0.090, 0.400, 0.080, 1)
-- INSERT INTO trapecios (tipo_seccion, posicion, base_inf, base_sup, altura, pieza_id) VALUES (2, 3, 0.090, 0.090, 0.280, 1)
-- INSERT INTO trapecios (tipo_seccion, posicion, base_inf, base_sup, altura, pieza_id) VALUES (2, 4, 0.400, 0.090, 0.080, 1)
-- INSERT INTO trapecios (tipo_seccion, posicion, base_inf, base_sup, altura, pieza_id) VALUES (2, 5, 0.400, 0.400, 0.080, 1)
