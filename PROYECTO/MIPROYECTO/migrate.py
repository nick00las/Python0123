import sqlite3

conn=sqlite3.connect('tienda.db')
cursor_obj = conn.cursor()
cursor_obj.execute("DROP TABLE IF EXISTS USUARIOS")
table = """ CREATE TABLE USUARIOS (
            ID  INTEGER PRIMARY KEY AUTOINCREMENT,
            USUARIO VARCHAR(25),
            PASSWORD VARCHAR(255) NOT NULL,
            EMAIL VARCHAR(255) NOT NULL,
            FULLNAME VARCHAR(25) NOT NULL,
            SCORE INT,
            TIPOUSUARIO VARCHAR(25)
        ); """
cursor_obj.execute(table)
cursor_obj.execute("DROP TABLE IF EXISTS PRODUCTOS")
table = """ CREATE TABLE PRODUCTOS (
            ID  INTEGER PRIMARY KEY AUTOINCREMENT,
            NAMEPRODUCT VARCHAR(255) NOT NULL,
            PRICE VARCHAR(20) NOT NULL, 
            CATEGORIA VARCHAR(25) NOT NULL,
            STCOKACTUAL INT,
            CREACTION_PRODUCT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UPDATE_PRODUCT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ); """
cursor_obj.execute(table)
cursor_obj.execute("DROP TABLE IF EXISTS VENTA")

table=""" CREATE TABLE VENTA (
            ORDERID  INTEGER PRIMARY KEY AUTOINCREMENT,
            PRODUCTID INT, 
            PRICETOTAL VARCHAR(25) NOT NULL
        ); """

cursor_obj.execute(table)
cursor_obj.execute("DROP TABLE IF EXISTS INVENTARIO")

table=""" CREATE TABLE INVENTARIO (
            IDMOVIMIENTO  INTEGER PRIMARY KEY AUTOINCREMENT,
            PRODUCTID INT NOT NULL, 
            CANTIDAD INT NOT NULL,
            FECHA_MOVIMIENTO TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ); """
cursor_obj.execute(table)

cursor_obj.execute("DROP TABLE IF EXISTS DOLAR")
table=""" CREATE TABLE DOLAR (
            IDKEY INTEGER PRIMARY KEY AUTOINCREMENT,
            DOLAR_SOLES FLOAT NOT NULL, 
            FECHA TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ); """
cursor_obj.execute(table)

conn.commit()
