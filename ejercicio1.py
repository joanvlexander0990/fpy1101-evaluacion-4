# =====================================================================
# EVALUACIÓN 4 - SISTEMA DE GESTIÓN DE BIBLIOTECA
# =====================================================================

# --- FUNCIÓN DEL MENÚ PRINCIPAL ---
def mostrar_menu():
    """Muestra las opciones del menú principal en pantalla."""
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    """Lee y retorna la opción elegida por el usuario validada."""
    try:
        opcion = int(input("Seleccione una opción: "))
        return opcion
    except ValueError:
        return 0

# --- FUNCIONES DE VALIDACIÓN (OPCIÓN 1) ---
def validar_titulo(titulo):
    """Retorna True si el título no está vacío ni contiene solo espacios."""
    return titulo.strip() != ""

def validar_copias(copias):
    """Retorna True si las copias son un entero mayor o igual a cero."""
    return copias >= 0

def validar_prestamo(prestamo):
    """Retorna True si el período de préstamo es mayor a cero."""
    return prestamo > 0

# --- FUNCIONES DE OPERACIONES ---

# Opción 1: Agregar libro
def agregar_libro(lista_libros):
    """Solicita, valida y agrega un nuevo libro a la lista."""
    titulo = input("Ingrese el título del libro: ")
    if not validar_titulo(titulo):
        print("Error: El nombre no puede estar vacío ni ser solo espacios en blanco.")
        return

    try:
        copias = int(input("Ingrese la cantidad de copias: "))
        if not validar_copias(copias):
            print("Error: Las copias deben ser un número entero mayor o igual que cero.")
            return
    except ValueError:
        print("Error: Las copias deben ser un número entero.")
        return

    try:
        prestamo = int(input("Ingrese el período de préstamo (en días): "))
        if not validar_prestamo(prestamo):
            print("Error: El período de préstamo debe ser un número entero mayor que cero.")
            return
    except ValueError:
        print("Error: El período de préstamo debe ser un número entero.")
        return

    # Si todo es válido, creamos el diccionario
    nuevo_libro = {
        "titulo": titulo,
        "copias": copias,
        "prestamo": prestamo,
        "disponible": False  # Inicia en False por defecto según restricción
    }
    lista_libros.append(nuevo_libro)
    print(f"Libro '{titulo}' registrado exitosamente.")

# Opción 2: Buscar libro
def buscar_libro(lista_libros, titulo_buscar):
    """Busca un libro por coincidencia exacta y retorna su índice o -1."""
    for i in range(len(lista_libros)):
        if lista_libros[i]["titulo"] == titulo_buscar:
            return i
    return -1

# Opción 4: Actualizar disponibilidad
def actualizar_disponibilidad(lista_libros):
    """Actualiza el campo disponible de todos los libros según sus copias."""
    for libro in lista_libros:
        if libro["copias"] >= 1:
            libro["disponible"] = True
        else:
            libro["disponible"] = False

# Opción 5: Mostrar libros
def mostrar_libros(lista_libros):
    """Actualiza y muestra en pantalla la lista de libros registrados."""
    # Primero actualiza la disponibilidad automáticamente
    actualizar_disponibilidad(lista_libros)
    
    print("\n=== LISTA DE LIBROS ===")
    if not lista_libros:
        print("No hay libros registrados.")
        return
        
    for libro in lista_libros:
        estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
        print(f"Título: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Préstamo: {libro['prestamo']}")
        print(f"Estado: {estado}")
        print("********************************************")


# --- PROGRAMA PRINCIPAL (FLUJO DE EJECUCIÓN) ---
def main():
    # La lista general de libros inicia vacía
    biblioteca = []
    
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        
        if opcion == 1:
            agregar_libro(biblioteca)
            
        elif opcion == 2:
            titulo_buscar = input("Ingrese el título del libro a buscar: ")
            posicion = buscar_libro(biblioteca, titulo_buscar)
            if posicion != -1:
                libro = biblioteca[posicion]
                print(f"\n[Libro Encontrado en posición {posicion}]")
                print(f"Título: {libro['titulo']}")
                print(f"Copias: {libro['copias']}")
                print(f"Préstamo: {libro['prestamo']}")
                estado_temp = "DISPONIBLE" if libro['copias'] >= 1 else "SIN COPIAS"
                print(f"Estado: {estado_temp}")
            else:
                print("Libro no encontrado.")
                
        elif opcion == 3:
            titulo_eliminar = input("Ingrese el título del libro que desea eliminar: ")
            posicion = buscar_libro(biblioteca, titulo_eliminar)
            if posicion != -1:
                biblioteca.pop(posicion)
                print(f"El libro '{titulo_eliminar}' fue eliminado exitosamente.")
            else:
                print(f"El libro '{titulo_eliminar}' no se encuentra registrado.")
                
        elif opcion == 4:
            actualizar_disponibilidad(biblioteca)
            print("Disponibilidad de todos los libros actualizada correctamente.")
            
        elif opcion == 5:
            mostrar_libros(biblioteca)
            
        elif opcion == 6:
            print("“Gracias por usar el sistema. Vuelva Pronto”")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
