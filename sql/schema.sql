
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
    'ventas' FLOAT,
    'total_ventas' FLOAT
);


CREATE TABLE PUBLIC.cliente (
    'id_cliente' INTEGER,
    'nombrecliente' VARCHAR
);


CREATE TABLE PUBLIC.descripcion (
    'id_descripcion' INTEGER,
    'descripcion' VARCHAR
);


CREATE TABLE PUBLIC.tipo_producto (
    'id_tipoproducto' INTEGER,
    'tipoproducto' VARCHAR
);


CREATE TABLE PUBLIC.localidad (
    'id_localidad' INTEGER,
    'localidad' VARCHAR
);


CREATE TABLE PUBLIC.sede (
    'id_sede' INTEGER,
    'sede' VARCHAR,
    'area' INTEGER
);

CREATE TABLE PUBLIC.empleados (
    'id_empleado' INTEGER,
    'Nombre_apellido' VARCHAR
);

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



