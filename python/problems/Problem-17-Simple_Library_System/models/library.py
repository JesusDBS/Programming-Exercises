from .librarian import Librarian
from .user import User
from .book import Book


class Library:
    users = []
    librarians = []
    books = []
    pending_borrows = []

    @classmethod
    def agregar_usuario(cls, nombre: str, apellido: str, dni: int):
        user = User(
            nombre=nombre,
            apellido=apellido,
            dni=dni
        )
        cls.users.append(user)

    @classmethod
    def agregar_librero(cls, nombre: str, apellido: str, dni: int):
        cls.librarians.append(
            Librarian(
                nombre=nombre,
                apellido=apellido,
                dni=dni
            )
        )

    @classmethod
    def agregar_libro(cls,
                      titulo: str,
                      categoria: str,
                      autor: str,
                      idioma: str,
                      unidades: int):
        book = Book(
            titulo=titulo,
            categoria=categoria,
            autor=autor,
            idioma=idioma,
            unidades=unidades
        )
        cls.books.append(book)

    @classmethod
    def listar_libros(cls):
        print('Libros')
        for book in cls.books:
            print(f'Titulo: {book.titulo}, Autor: {book.autor}')

    @classmethod
    def listar_libreros_activos(cls):
        print('Libreros activos:')
        for librero in cls.librarians:
            if librero.active:
                print(f'{librero.full_name}')

    @classmethod
    def listar_libreros(cls):
        print('Libreros:')
        for librero in cls.librarians:
            print(f'{librero.full_name}')

    @classmethod
    def listar_usuarios(cls):
        print('Usuarios')
        for user in cls.users:
            print(f'{user.full_name}')

    @classmethod
    def buscar_libro_por_nombre(cls, name: str):
        assert isinstance(name, str), f'El nombre: {name}, debe ser un string!'
        name = name.strip().lower()
        book = list(
            filter(lambda b: b.titulo.strip().lower() == name, cls.books))

        if book:
            return book

        print(f'No se ha encontrado el libro: {name}. Por favor verifique!')
        return False
