## Ejercicio 2

biblioteca = {
    "categoria": ["ficcion", "no-ficcion", "ciencia", "infantil"],
    "libros": [
        { "nombre": "El gran gatsby", "autor": "F. Scott Fitzgerald", "categoria": "ficcion", "estado": "disponible" },
        { "nombre": "la ciencia de la biología", "estado": "Jane B. Reece", "categoria": "ciencia", "estado": "disponible" },
        { "nombre": "la teñaraña de charlote", "autor": "E.B. White", "categoria": "infantil", "estado": "disponible" },
        { "nombre": "7 habitos altamente efectivos en las personas", "autor": "Stephen Covey", "categoria": "no-ficcion", "estado": "disponible" }
    ],
    "usuario": [
        { "nombre": "Juan Carrizales", "libros_prestado": [] },
        { "nombre": "Victor Hugo Alarcon", "libros_prestado": [] }
    ]
}

# funcion para ver la lista de categoria
def ver_categoria():
    return biblioteca["categoria"]

#  funcion para consultar el nombre del libro y el autor
def consultar_libro():
    libros = []
    for libro in biblioteca["libros"]:
        libros.append(f"{libro['nombre']} by {libro['autor']}")
    return libros

# funcion para cambiar es estado del libro a prestado
def pestrar_libro(libro_nombre):
    for libro in biblioteca["libros"]:
        if libro["nombre"] == libro_nombre:
            if libro["estado"] == "disponible":
                libro["estado"] = "prestado"
                return f"{libro_nombre} ha sido exitosamente prestado."
            else:
                return f"{libro_nombre} no pudo prestarse"
    return f"{libro_nombre} no se encontro en biblioteca."

# Function to get the list of usuario
def get_users():
    usuario = []
    for usuario in biblioteca["usuario"]:
        usuario.append(usuario["nombre"])
    return usuario