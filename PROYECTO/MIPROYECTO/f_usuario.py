import sqlite3

def leer_parametro_ur():
    usuario=input("Ingrese usuario: ")
    password=input("Ingrese contraseña ")
    email=input("Ingrese email: ")
    fullname=input("Ingrese nombre completo: ")
    score=input("Ingrese puntuación: ")
    tipousuario=input("Ingrese el tipo de usuario: ")
    return usuario,password,email,fullname,score,tipousuario


def crear_usuario():
    parametro=leer_parametro_ur()
    conn=sqlite3.connect('tienda.db')
    insert=f"INSERT INTO USUARIOS(USUARIO,PASSWORD,EMAIL,FULLNAME,SCORE,TIPOUSUARIO) VALUES {parametro}"
    conn.execute(insert)
    conn.commit()

def eliminar_usuario(usuario):
    #DELETE FROM table_name WHERE condition;
    conn=sqlite3.connect('tienda.db')
    delete=f"DELETE * FROM USUARIOS WHERE USUARIO={usuario}"
    conn.execute(delete)
    conn.commit()


def update_usuario(usuario,email):
    conn=sqlite3.connect('tienda.db')
    update=f"UPDATE USUARIOS SET USUARIO={usuario} WHERE EMAIL={email}"
    conn.execute(update)
    conn.commit()