from datetime import datetime


class Libro:
    def __init__(self, titulo, autor, paginas):
        """
        Constructor de la clase Libro

        Args:
            titulo (str): Título del libro
            autor (str): Autor del libro
            paginas (int): Número total de páginas
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = True

        # --- Característica extra (el toque "humano") ---
        # Guardamos quién tiene el libro actualmente y un historial
        # de todos los préstamos, como haría un bibliotecario real
        # anotando en una ficha de papel quién se llevó cada libro.
        self.prestado_a = None
        self.historial_prestamos = []

    def prestar(self, persona="alguien"):
        """
        Presta el libro a una persona en particular.

        Args:
            persona (str): Nombre de quien pide el libro prestado
        """
        if self.disponible:
            self.disponible = False
            self.prestado_a = persona
            fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
            self.historial_prestamos.append((persona, fecha))
            return f"'{self.titulo}' ha sido prestado a {persona} el {fecha}."
        else:
            return (f"'{self.titulo}' no está disponible en este momento. "
                    f"Actualmente lo tiene {self.prestado_a}.")

    def devolver(self):
        """
        Devuelve el libro a la biblioteca.
        """
        if not self.disponible:
            persona = self.prestado_a
            self.disponible = True
            self.prestado_a = None
            return f"'{self.titulo}' ha sido devuelto por {persona}. ¡Gracias!"
        else:
            return f"'{self.titulo}' ya estaba en la biblioteca."

    def informacion(self):
        """
        Devuelve toda la información del libro, incluyendo su estado
        de disponibilidad y quién lo tiene prestado (si aplica).
        """
        estado = "Disponible" if self.disponible else f"Prestado a {self.prestado_a}"
        info = (f"Título: {self.titulo}\n"
                f"Autor: {self.autor}\n"
                f"Páginas: {self.paginas}\n"
                f"Estado: {estado}\n"
                f"Veces prestado en total: {len(self.historial_prestamos)}")
        return info


# Prueba de la clase Libro
def main():
    # Crear dos objetos libro diferentes
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)

    # Mostrar información inicial de los libros
    print("=== Información inicial de los libros ===")
    print(libro1.informacion())
    print("\n")
    print(libro2.informacion())
    print("\n")

    # Prestar los libros
    print("=== Préstamo de libros ===")
    print(libro1.prestar("Juan"))
    print(libro2.prestar("María"))
    print("\n")

    # Intentar prestar un libro ya prestado
    print("=== Intento de préstamo de libros ya prestados ===")
    print(libro1.prestar("Carlos"))
    print("\n")

    # Mostrar información después del préstamo
    print("=== Información después del préstamo ===")
    print(libro1.informacion())
    print("\n")

    # Devolver un libro
    print("=== Devolución de libros ===")
    print(libro1.devolver())
    print("\n")

    # Intentar devolver un libro ya disponible
    print("=== Intento de devolución de libros ya disponibles ===")
    print(libro1.devolver())
    print("\n")

    # Mostrar información final
    print("=== Información final de los libros ===")
    print(libro1.informacion())
    print("\n")
    print(libro2.informacion())


if __name__ == "__main__":
    main()