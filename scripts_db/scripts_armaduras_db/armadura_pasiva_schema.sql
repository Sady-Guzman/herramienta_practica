-- TABLAS PARA MANEJAR ARMADURA PASIVA.
-- tipo armadura corresponde a los distintos tipos de cableados que conforman a la armadura pasiva: Barra Corrugada, Cerco, Malla
-- Material: Todos los materiales estan disponibles para los 3 tipos de armaduras.
-- USO: Flexion, Cortante, Varios, Flexion aleta, Cortante aleta... No entiendo estos terminos. estan en jacena

-- Creacion de tablas:

CREATE TABLE IF NOT EXISTS apasiva_tipos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_tipo TEXT,
);

CREATE TABLE  IF NOT EXISTS apasiva_materiales (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    nombre_material TEXT,
};

CREATE TABLE  IF NOT EXISTS apasiva_usos (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    nombre_uso TEXT,
};

-- Inserts de valores que existen en jacena para pantalla de Armaduras Pasivas

INSERT INTO apasiva_tipos (nombre_tipo)
    VALUES ("Barra Corrugada"), ("Cerco"), ("Malla");

INSERT INTO apasiva_tipos (nombre_material)
    VALUES ("Barra Corrugada"), ("Cerco"), ("Malla");

INSERT INTO apasiva_tipos (nombre_uso)
    VALUES ("Flexión"), ("Cortante"), ("Varios"), ("Flexión Aleta"), ("Cortante Aleta");
