-- Creacion de tablas para base de datos materiales.db

-- tipos de hormigon existentes disponibles
CREATE TABLE tipos_hormigon(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_tipo TEXT UNIQUE
);

-- Datos para correspondiente f'_c (Resistecia hormigon), Para campos de Fck(f'c)(N/mm2) y E(N/mm2)
CREATE TABLE resistencias_hormigon(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_hormigon INTEGER NOT NULL,
    fc_horm_ini_min REAL,
    e_horm_ini_min REAL,
    fc_horm_ini_max REAL,
    e_horm_ini_max REAL,
    fc_horm_final REAL,
    e_horm_final REAL,
    fc_horm_insitu REAL,
    e_horm_insitu REAL,
    FOREIGN KEY (tipo_hormigon) REFERENCES tipo_hormigon(id)
);

-- datos para campos de densidad hormigon / acero que se llenan automaticamente segun tipo de hormigon seleccionado.
CREATE TABLE densidades(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_hormigon INTEGER NOT NULL,
    dens_horm REAL,
    dens_acero REAL,
    FOREIGN KEY (tipo_hormigon) REFERENCES tipo_hormigon(id)
);


-- Inserts para tipos de hormigon existentes
INSERT INTO tipos_hormigon(nombre_tipo)
VALUES ("f'c 450/10"), ("f'c 350/20"), ("f'c 450/20 DALLA"), ("f'c 450/20 ALV"), ("f'c 500/20"), ("f'c 450/10 CAN"), ("f'c 400/20"), ("HA 25"), ("HP 50");

-- Inserts para resistencias segun tipo hormigon
INSERT INTO resistencias_hormigon(tipo_hormigon, fc_horm_ini_min, e_horm_ini_min, fc_horm_ini_max, e_horm_ini_max, fc_horm_final, e_horm_final, fc_horm_insitu, e_horm_insitu)
VALUES 
(1, 25, 23500, 35, 23500, 45, 31528, 25, 23500),
(2, 20, 21019, 25, 21019, 35, 27806, 25, 23500);

-- Inserts para densidades segun tipo de hormigon
INSERT INTO densidades(tipo_hormigon, dens_horm, dens_acero)
VALUES
(1, 25, 78.5),
(2, 25, 78.5);
