import sqlite3

def leer_parametro_ur():
    usuario=input("Ingrese usuario: ")
    password=input("Ingrese contraseña: ")
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
    if comprobar_vacio() is False:
        #DELETE FROM table_name WHERE condition;
        conn=sqlite3.connect('tienda.db')
        delete=f"DELETE FROM USUARIOS WHERE USUARIO='{usuario}'"
        conn.execute(delete)
        conn.commit()
    else:
        pass

def update_usuario(usuario,email):
    if comprobar_vacio() is False:
        conn=sqlite3.connect('tienda.db')
        update=f"UPDATE USUARIOS SET USUARIO='{usuario}' WHERE EMAIL='{email}'"
        conn.execute(update)
        conn.commit()
    else:
        pass

def contar_filas():
    # Conectarse a la base de datos
    conn = sqlite3.connect('tienda.db')
    cursor = conn.cursor()

    # Nombre de la tabla a verificar
    nombre_tabla = 'USUARIOS'

    # Consulta SQL para contar el número de filas en la tabla
    consulta = f"SELECT COUNT(*) FROM {nombre_tabla}"
    cursor.execute(consulta)

    # Obtener el resultado de la consulta
    filas = cursor.fetchone()[0]

    # Cerrar la conexión a la base de datos
    conn.close()

    return filas

def comprobar_vacio():
        # Comprobar si la tabla está vacía
    filas=contar_filas()
    if filas == 0:
        return True
    else:
        pass