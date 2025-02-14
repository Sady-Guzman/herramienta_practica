-- schema de tabla
CREATE TABLE "testeros" (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    testero TEXT NOT NULL,
    posicion INTEGER NOT NULL, 
    cota REAL NOT NULL);


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



-- Inserts de pos/cota de TESTERO 0.50 PULGADAS
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 1, 0.040);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 2, 0.090);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 3, 0.140);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 4, 0.190);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 5, 0.240);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 6, 0.290);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 7, 0.340);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 8, 0.390);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 9, 0.440);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 10, 0.490);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 11, 0.540);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 12, 0.590);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 13, 0.640);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 14, 0.690);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 15, 0.740);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 16, 0.790);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 17, 0.840);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 18, 0.890);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 19, 0.940);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 20, 0.990);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 21, 1.040);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 22, 1.090);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 23, 1.140);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 24, 1.190);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 25, 1.240);
INSERT INTO testeros (testero, posicion, cota) VALUES ("ESTANDAR/0.5''", 26, 1.290);

--  generado con:
-- altura = 0.040

-- for i in range(30):
--     print(f"INSERT INTO testeros (testero, posicion, cota) VALUES (\"ESTANDAR/0.5\'\'\", {i+1}, {altura:.3f});")
--     altura += 0.050
