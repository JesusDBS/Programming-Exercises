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
        return self.name + self.apellido

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

    def solicitar_prestamo(self, book: Book, pending_borrow: list):
        if book.mostrar_disponibilidad():
            borrow_vals = {
                'user': self,
                'book': book,
                'status': 'waiting'
            }
            pending_borrow.append(borrow_vals)
        raise Exception(
            'NO HAY DISPONIBILIDAD PARA ESTE LIBRO: {}'.format(book.titulo))

    def chequear_solvencia(self):
        print(f'El usuario {self.full_name}, con DNI: {self.dni} se encuentra {'suspendido.' if not self.solvente else 'al día.'}')

        return self.solvente

    def mis_prestamos(self):
        if self.prestamos:
            for prestamo in self.prestamos:
                print(prestamo)
        raise Exception('ACTUALMENTE ESTE USUARIO NO TIENE LIBROS')

    def leer_libro(self, book: Book):
        print(f'Leyendo {book.titulo}...')
