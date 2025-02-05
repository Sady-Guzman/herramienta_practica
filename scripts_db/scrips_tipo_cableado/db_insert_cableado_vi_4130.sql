
-- !!! Guarda inserts usados para llenar DB armaduras.db con tipos_cableados (presets configuracion de cordones) para ejemplo en software
-- PK tipo_cableado en cableado_cables no deberia estar hard-codeado.
-- Automatizar con tipo_cableado_id = cursor.lastrowid en caso de querer usar como script

-- CH 31 - T2
INSERT INTO cableado_tipos (familia, modelo, tipo_cableado) VALUES ('CH', '31', 'T2');

INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('32', '0.190', '12.7', '0', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('32', '0.140', '12.7', '0', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('32', '0.090', '12.7', '0', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('32', '0.040', '12.7', '2', '1400');
--

-- CH 51 - T4
INSERT INTO cableado_tipos (familia, modelo, tipo_cableado) VALUES ('CH', '51', 'T4');

INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('33', '0.190', '12.7', '2', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('33', '0.140', '12.7', '0', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('33', '0.090', '12.7', '2', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('33', '0.040', '12.7', '0', '1400');
--

-- CH 51 - T5
INSERT INTO cableado_tipos (familia, modelo, tipo_cableado) VALUES ('CH', '51', 'T5');

INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('34', '0.190', '12.7', '0', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('34', '0.140', '12.7', '2', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('34', '0.090', '12.7', '0', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('34', '0.040', '12.7', '2', '1400');
--
