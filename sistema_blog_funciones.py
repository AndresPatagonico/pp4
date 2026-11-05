"""
    Pre entrega 4
    Vemos funciones modulares.
"""

# Perfil autor.
perfil_autor = {
    "nombre": "Bel Arena",
    "bio": "Desarrolladora web y creadora de contenido sobre programación.",
    "especialidad": "Python y Django",
    "redes_sociales": ["@bel_dev", "@bel_python"]
}

# Estados post.
estados_post = ("borrador", "publicado", "archivado")

# Etiquetas Blog.
etiquetas_blog = {"Python", "Django", "Web", "Backend", "Python"}

# Post.
posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "En este post veremos cómo empezar a programar con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Qué es Django",
        "contenido": "Django es un framework web creado con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "Web"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con listas",
        "contenido": "Las listas permiten guardar varios elementos en una sola variable.",
        "autor": perfil_autor,
        "tags": ["Python", "Listas"],
        "estado": "archivado"
    }
]

# ###########
# Funciones.
# ###########

# Muestra el menu.
def mostrar_menu():
    print("\n<--- MENÚ DEL BLOG --->")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")
    print("-----------------------")
    
    try:
        opcion = int(input("Seleccione una opción (1 a 5): ")) # int = convierte lo ingresado en un entero.
        return opcion
    except ValueError: # Maneja el error si el usuario ingresa un valor no esperado.
        print("Opción no válida. Por favor, ingrese un número entre 1 y 5.")
        return None
    
# Recorre la lista de post, muestra el titulo y nombre del autor.
def listar_posts(lista):
    if not lista:
        print("No hay posts para mostrar.")
        return
    
    print("\n") # \n hace saltos de linea.
    print("Listado de posts")
    for post in lista: 
        titulo = post.get("titulo", "Sin titulo")   # get(clave a buscar, valor por defecto)
        autor_dict = post.get("autor")
        
        if isinstance(autor_dict, dict): # Verificamos que el autor sea un diccionario para extraer el nombre.
            nombre_autor = autor_dict.get("nombre", "Autor desconocido")
        else:
            nombre_autor = "Autor no válido"
    
        print(f"Titulo: {titulo} Autor: {nombre_autor}")


# Busca y muestra posts cuyo titulo contenga el termino
def buscar_por_titulo(lista, termino):
    if not termino.strip():
        print("La busqueda no puede estar vacia.")
        
    
    termino_minusculas = termino.lower()
    resultados = []
    
    for post in lista:
        titulo = post.get("titulo", "")
        if termino_minusculas in titulo.lower():
            resultados.append(post)
            
    
    if resultados:
        print(f"Resultados para la busqueda '{termino}': ")
        listar_posts(resultados)
    else:
        print(f"No se encontraron posts que contengan '{termino}' ")
        

# Filtra y muestra posts que contengan un tag especifico
def filtrar_por_tag(lista, tag):
    if not tag.strip():
        print("El tag de busqueda no puede estar vacio.")
        return
    
    tag_minusculas = tag.lower()
    resultados = []
    
    for post in lista:
        tags = post.get("tags", [])
        if isinstance(tags, list):
            tags_lower = [t.lower() for t in tags]
            if tag_minusculas in tags_lower:
                resultados.append(post)

    if resultados:
        print(f"Posts con el tag '{tag}':")
        listar_posts(resultados)
    else:
        print(f"No se encontraron posts con el tag '{tag}'.")

# Verifica si un post cumple con todas las reglas estructurales y de datos.
def validar_post(post):
    if not isinstance(post, dict):
        return "Error: El post no es un diccionario."

    # Claves obligatorias que deben existir
    claves_necesarias = ["id", "titulo", "contenido", "autor", "tags", "estado"]
    for clave in claves_necesarias:
        if clave not in post:
            return f"Error: Falta la clave obligatoria '{clave}'."

    # Validar que el título no esté vacío
    if not post["titulo"].strip():
        return "Error: El título no puede estar vacío."

    # Validar que el contenido no esté vacío
    if not post["contenido"].strip():
        return "Error: El contenido no puede estar vacío."

    # Validar que el autor sea un diccionario y tenga la clave "nombre"
    autor = post["autor"]
    if not isinstance(autor, dict) or "nombre" not in autor:
        return "Error: La clave 'autor' debe ser un diccionario válido con la clave 'nombre'."

    # Validar que los tags sean una lista
    if not isinstance(post["tags"], list):
        return "Error: La clave 'tags' debe ser una lista."

    # Validar que el estado pertenezca a la tupla permitida
    if post["estado"] not in estados_post:
        return f"Error: El estado '{post['estado']}' no es válido. Debe ser uno de {estados_post}."

    return True


# ################
# Bucle principal
# ################
if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            listar_posts(posts)

        elif opcion == 2:
            termino = input("Ingrese el título o palabra a buscar: ")
            buscar_por_titulo(posts, termino)

        elif opcion == 3:
            tag_buscado = input("Ingrese el tag a filtrar: ")
            filtrar_por_tag(posts, tag_buscado)

        elif opcion == 4:
            print("--- VALIDACIÓN DE POSTS ---")
            for i, post in enumerate(posts, start=1):
                resultado = validar_post(post)
                if resultado is True:
                    print(f"Post {i}: Válido")
                else:
                    print(f"Post {i}: {resultado}")

        elif opcion == 5:
            print("\nGracias vuelvas prontos")
            break

        else:
            if opcion is not None:
                print("Opción no válida. Por favor, elegí un número del 1 al 5.")