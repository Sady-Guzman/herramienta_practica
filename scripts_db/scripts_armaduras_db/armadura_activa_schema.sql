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



-- INSERTS PARA tabla de propiedades de armaduras activas:

INSERT INTO propiedades_armadura_activa (nombre_comun, acero_completo, acero_corto, diametro, masa, area, carga_rotura, limmite_elastico)
    VALUES ('Alambre 5mm', 'ASTM-421M Grado 1655 R2', 'ASTM-421M', 4.98, 0.153, 0.195, 32.2, 29);

INSERT INTO propiedades_armadura_activa (nombre_comun, acero_completo, acero_corto, diametro, masa, area, carga_rotura, limmite_elastico)
    VALUES ('Cordon 3/8''''', 'ASTM-416M Grado 1860 R2', 'ASTM-416M', 9.53, 0.432, 0.548, 102.3, 92.1);

INSERT INTO propiedades_armadura_activa (nombre_comun, acero_completo, acero_corto, diametro, masa, area, carga_rotura, limmite_elastico)
    VALUES ('Cordon 1/2''''', 'ASTM-416M Grado 1860 R2', 'ASTM-416M', 12.7, 0.775, 0.987, 183.7, 165.3);

INSERT INTO propiedades_armadura_activa (nombre_comun, acero_completo, acero_corto, diametro, masa, area, carga_rotura, limmite_elastico)
    VALUES ('Cordon 0.6''''', 'ASTM-416M Grado 1860 R2', 'ASTM-416M', 15.24, 1.102, 1.400, 260.7, 234.6);

--  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--  Tabla unidades no se usa por ahora
CREATE TABLE unidades(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre_medida TEXT,
unidad TEXT);

INSERT INTO unidades (nombre_medida, unidad) VALUES ('cota', 'metros [m]');
INSERT INTO unidades (nombre_medida, unidad) VALUES ('diametro', 'phi milimetros [mm]');
INSERT INTO unidades (nombre_medida, unidad) VALUES ('masa', 'kilogramos/metro [kg/m]');
INSERT INTO unidades (nombre_medida, unidad) VALUES ('area', 'centrimetros cuadrados [cm2]');
INSERT INTO unidades (nombre_medida, unidad) VALUES ('carga de rotura', 'Kilo Newton [kN]');
INSERT INTO unidades (nombre_medida, unidad) VALUES ('limite elastico', 'Kilo Newton [kN]');

--  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------


-- Presets
-- Tipos: T2, T4, T6, T.... (Informacion cableados estandar en carpeta 410)
CREATE TABLE cableado_tipos (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    familia TEXT NOT NULL,
    modelo TEXT NOT NULL, 
    tipo_cableado TEXT NOT NULL);


CREATE TABLE cableado_cables (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    tipo_cableado INTEGER NOT NULL,
    cota REAL NOT NULL,
    diametro REAL NOT NULL,
    num_cord INTEGER NOT NULL,
    tpi REAL NOT NULL,
    FOREIGN KEY (tipo_cableado) REFERENCES cableado_tipos(id)
);

-- INSERTS DE CABLEADOS ESTANDAR se guardan en carpeta especial. Usando un archivo por cada pieza
-- (Cada pieza tiene varios tipos de cableado estandar)