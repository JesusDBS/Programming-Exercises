# -------------------------------------------
# Library Management System
# Create a system to manage a library's book inventory, borrowers, and borrowing transactions.

# Classes to implement: Book, Member, Librarian, Library.
# Features:
# 1) Add, remove, and search for books.
# 2) Register new members.
# 3) Borrow and return books.
# 4) Track borrowing history.
# -------------------------------------------

from models.library import Library
from models.book import Book
from models.user import User
from models.librarian import Librarian

if __name__ == '__main__':

    MyLibrary = Library()
    book1 = {
        'title': '1984',
        'categoria': 'distopía',
        'autor': 'George Orwell',
        'idioma': 'English',
        'unidades': 5
    }
    book2 = {
        'title': 'Un mundo feliz',
        'categoria': 'distopía',
        'autor': 'Aldous Huxley',
        'idioma': 'English',
        'unidades': 4
    }
    book3 = {
        'title': '100 años de soledad',
        'categoria': 'realismo mágico',
        'autor': 'Gabriel García Márquez',
        'idioma': 'Spanish',
        'unidades': 3
    }

    books = [book1, book2, book3]
    for book in books:
        MyLibrary.agregar_libro(
            titulo=book['title'],
            categoria=book['categoria'],
            autor=book['autor'],
            idioma=book['idioma'],
            unidades=book['unidades']
        )
    MyLibrary.listar_libros()

    print('\n')
    user1 = {
        'nombre': 'Juan',
        'apellido': 'Perez',
        'dni': 12345678
    }
    user2 = {
        'nombre': 'Maria',
        'apellido': 'Gonzalez',
        'dni': 87654321
    }
    users = [user1, user2]
    for user in users:
        MyLibrary.agregar_usuario(
            nombre=user['nombre'],
            apellido=user['apellido'],
            dni=user['dni']
        )
    MyLibrary.listar_usuarios()

    print('\n')
    book = MyLibrary.buscar_libro_por_nombre('1984')
    print(book)
    book = MyLibrary.buscar_libro_por_nombre('Un mundo')

    print('\n')
    MyLibrary.agregar_librero(
        nombre='Juan',
        apellido='Gomez',
        dni=11111111
    )
    MyLibrary.listar_libreros()
    print(MyLibrary.librarians[0])
    print(MyLibrary.librarians[0].full_name)
    print(MyLibrary.librarians[0].activo)

    print('\n')
    user1 = MyLibrary.users[0]
    print(user1)

    print('\n')
    user1.solicitar_prestamo(
        book=MyLibrary.books[0], pending_borrows=MyLibrary.pending_borrows)

    print(MyLibrary.pending_borrows)
    user1.mis_prestamos()

    print('\n')
    MyLibrary.librarians[0].aprobar_prestamos(MyLibrary.pending_borrows)
    user1.mis_prestamos()
    MyLibrary.books[0].mostrar_disponibilidad()
    user1.devolver_libro(MyLibrary.books[0])
    MyLibrary.books[0].mostrar_disponibilidad()
