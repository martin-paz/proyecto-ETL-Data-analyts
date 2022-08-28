DROP TABLE IF EXISTS venta;
CREATE TABLE PUBLIC.venta (
    'id_venta' INTEGER,
    'fecha' DATE,
    'id_cliente' INTEGER,
    'id_empleado' INTEGER,
    'id_tipoproducto' INTEGER,
    'id_descripcion' INTEGER,
    'id_localidad' INTEGER,
    'id_sede' INTEGER,
    'cantidad' INTEGER,
    'ventas' REAL,
    'total_ventas_usd' REAL
);
COPY PUBLIC.transaction FROM 'C:/Users/Public/data/auto_motors/venta.csv' DELIMITER ',' CSV HEADER;


DROP TABLE IF EXISTS cliente;
CREATE TABLE PUBLIC.cliente (
    'id_cliente' INTEGER,
    'nombrecliente' TEXT
);
COPY PUBLIC.transaction FROM 'C:/Users/Public/data/auto_motors/cliente.csv' DELIMITER ',' CSV HEADER;


DROP TABLE IF EXISTS descripcion;
CREATE TABLE PUBLIC.descripcion (
    'id_descripcion' INTEGER,
    'descripcion' TEXT
);
COPY PUBLIC.transaction FROM 'C:/Users/Public/data/auto_motors/descripcion.csv' DELIMITER ',' CSV HEADER;


DROP TABLE IF EXISTS tipo_producto;
CREATE TABLE PUBLIC.tipo_producto (
    'id_tipoproducto' INTEGER,
    'tipoproducto' TEXT
);
COPY PUBLIC.transaction FROM 'C:/Users/Public/data/auto_motors/tipo_producto.csv' DELIMITER ',' CSV HEADER;


DROP TABLE IF EXISTS localidad;
CREATE TABLE PUBLIC.localidad (
    'id_localidad' INTEGER,
    'localidad' TEXT
);
COPY PUBLIC.transaction FROM 'C:/Users/Public/data/auto_motors/localidad.csv' DELIMITER ',' CSV HEADER;


DROP TABLE IF EXISTS sede;
CREATE TABLE PUBLIC.sede (
    'id_sede' INTEGER,
    'sede' TEXT,
    'area' INTEGER
);
COPY PUBLIC.transaction FROM 'C:/Users/Public/data/auto_motors/sede.csv' DELIMITER ',' CSV HEADER;


DROP TABLE IF EXISTS empleados;
CREATE TABLE PUBLIC.empleados (
    'id_empleado' INTEGER,
    'Nombre_apellido' TEXT
);
COPY PUBLIC.transaction FROM 'C:/Users/Public/data/auto_motors/empleados.csv' DELIMITER ',' CSV HEADER;



-- CREACION DE LAS RELACIONES


-- Primary keys table
ALTER TABLE 'venta' ADD PRIMARY KEY ('id_venta');
ALTER TABLE 'cliente' ADD PRIMARY KEY ('id_cliente');
ALTER TABLE 'empleados' ADD PRIMARY KEY ('id_empleado');
ALTER TABLE 'tipo_producto' ADD PRIMARY KEY ('id_tipoproducto');
ALTER TABLE 'descripcion' ADD PRIMARY KEY ('id_descripcion');
ALTER TABLE 'localidad' ADD PRIMARY KEY ('id_localidad');
ALTER TABLE 'sede' ADD PRIMARY KEY ('id_sede');


-- Relations - venta -> cliente
ALTER TABLE 'venta' 
ADD CONSTRAINT 'venta_cliente_fk'
FOREIGN KEY ('id_cliente')
REFERENCES 'cliente'('id_cliente')


-- Relations - venta -> empleados
ALTER TABLE 'venta'
ADD CONSTRAINT 'venta_empleados_fk'
FOREIGN KEY ('id_empleado')
REFERENCES 'empleados'('id_empleado')


-- Relations - venta -> tipo_producto
ALTER TABLE 'venta'
ADD CONSTRAINT 'venta_tipoproducto_fk'
FOREIGN KEY ('id_tipoproducto')
REFERENCES 'tipoproducto'('id_tipoproducto')


-- Relations - venta -> descripcion
ALTER TABLE 'venta'
ADD CONSTRAINT 'venta_descripcion_fk'
FOREIGN KEY ('id_descripcion')
REFERENCES 'descripcion'('id_descripcion')


-- Relations - venta -> localidad
ALTER TABLE 'venta'
ADD CONSTRAINT 'venta_localidad_fk'
FOREIGN KEY ('id_localidad')
REFERENCES 'localidad'('id_localidad')


-- Relations - venta -> sede
ALTER TABLE 'venta'
ADD CONSTRAINT 'venta_sede_fk'
FOREIGN KEY ('id_sede')
REFERENCES 'sede'('id_sede')



