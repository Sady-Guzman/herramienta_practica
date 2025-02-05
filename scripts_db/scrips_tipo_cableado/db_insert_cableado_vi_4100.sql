
-- !!! Guarda inserts usados para llenar DB armaduras.db con tipos_cableados (presets configuracion de cordones) para ejemplo en software
-- PK tipo_cableado en cableado_cables no deberia estar hard-codeado.
-- Automatizar con tipo_cableado_id = cursor.lastrowid en caso de querer usar como script

-- VI 4100 T8
INSERT INTO cableado_tipos (familia, modelo, tipo_cableado) VALUES ('VI', '4100', 'T8');

INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('16', '0.950', '9.53', '2', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('16', '0.170', '9.53', '0', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('16', '0.110', '9.53', '0', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('16', '0.050', '9.53', '0', '1400');

INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('16', '0.950', '15.24', '0', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('16', '0.170', '15.24', '0', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('16', '0.110', '15.24', '1', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('16', '0.050', '15.24', '5', '1400');
--

-- VI 4100 T10
INSERT INTO cableado_tipos (familia, modelo, tipo_cableado) VALUES ('VI', '4100', 'T10');

INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('17', '0.950', '9.53', '2', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('17', '0.170', '9.53', '0', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('17', '0.110', '9.53', '0', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('17', '0.050', '9.53', '0', '1400');

INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('17', '0.950', '15.24', '0', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('17', '0.170', '15.24', '0', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('17', '0.110', '15.24', '3', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('17', '0.050', '15.24', '5', '1400');
--

-- VI 4100 T12
INSERT INTO cableado_tipos (familia, modelo, tipo_cableado) VALUES ('VI', '4100', 'T12');

INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('18', '0.950', '15.24', '2', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('18', '0.170', '15.24', '0', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('18', '0.110', '15.24', '5', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('18', '0.050', '15.24', '5', '1400');
--


-- VI 4100 T14
INSERT INTO cableado_tipos (familia, modelo, tipo_cableado) VALUES ('VI', '4100', 'T14');

INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('19', '0.950', '15.24', '2', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('19', '0.170', '15.24', '2', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('19', '0.110', '15.24', '5', '1400');
INSERT INTO cableado_cables (tipo_cableado, cota, diametro, num_cord, tpi) VALUES ('19', '0.050', '15.24', '5', '1400');
--
