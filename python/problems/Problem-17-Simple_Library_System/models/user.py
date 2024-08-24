from .book import Book


class User:
    def __init__(self,
                 nombre: str,
                 apellido: str,
                 dni: int) -> None:

        assert isinstance(nombre, str), f"EL NOMBRE DEBE SER UN STRING!"
        assert isinstance(apellido, str), f"EL APELLIDO DEBE SER UN STRING!"
        assert isinstance(dni, int), f"EL DNI DEBE SER UN ENTERO!"

        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

        self.__solvente = True
        self.__prestamos = []

    @property
    def full_name(self):
        return self.nombre + ' ' + self.apellido

    @property
    def prestamos(self):
        return self.__prestamos

    @property
    def solvente(self):
        return self.__solvente

    @solvente.setter
    def solvente(self, solvencia: bool):
        if isinstance(solvencia, bool):
            self.__solvente = solvencia
            return self.__solvente
        raise ValueError('LA SOLVENCIA DEBE SER UN BOOLEANO')

    def solicitar_prestamo(self, book: Book, pending_borrows: list):
        if book.mostrar_disponibilidad():
            print(f'El libro {book.titulo} está disponible')
            borrow_vals = {
                'user': self,
                'book': book,
                'status': 'waiting'
            }
            pending_borrows.append(borrow_vals)
            return True
        raise Exception(
            'NO HAY DISPONIBILIDAD PARA ESTE LIBRO: {}'.format(book.titulo))

    def chequear_solvencia(self):
        print(
            f'El usuario {self.full_name}, con DNI: {self.dni} se encuentra {"suspendido." if not self.solvente else "al día."}')

        return self.solvente

    def mis_prestamos(self):
        print(f'PRESTAMOS DE {self.full_name}')
        if self.prestamos:
            for prestamo in self.prestamos:
                print(prestamo)
                return True
        print('ACTUALMENTE ESTE USUARIO NO TIENE LIBROS')

    def leer_libro(self, book: Book):
        print(f'Leyendo {book.titulo}...')

    def agregar_prestamo(self, prestamo: dict):
        if isinstance(prestamo, dict):
            self.__prestamos.append(prestamo)
            return True
        raise Exception('El prestamo debe ser un diccionario!')

    def devolver_libro(self, book: Book):
        for prestamo in self.prestamos:
            prestamo['book'].devolver_libro(user=self)

    def __str__(self) -> str:
        return f"{self.full_name} ({self.dni})"
