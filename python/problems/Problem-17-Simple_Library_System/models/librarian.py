from datetime import datetime, timedelta
from .user import User


class Librarian(User):
    def __init__(self, nombre: str, apellido: str, dni: int) -> None:
        super().__init__(nombre, apellido, dni)
        self.activo = True

    @staticmethod
    def __date_2_string(date: datetime, format: str = '%d/%m/%Y') -> str:
        return date.strftime(format)

    def __get_return_date(self, date: datetime, days: int = 3, format: str = '%d/%m/%Y') -> str:
        return_date = date + timedelta(days=days)
        return self.__date_2_string(return_date, format=format)

    def aprobar_prestamos(self, pending_borrows: list):
        if len(pending_borrows) == 0:
            print('No hay prestamos pendientes por aprobar')
            return False

        for borrow in pending_borrows:
            if borrow['status'] == 'waiting':
                if borrow['book'].mostrar_disponibilidad:
                    borrow['book'].prestar_libro(borrow['user'])
                    borrow_vals = {
                        'book': borrow['book'],
                        'borrow_date': self.__date_2_string(datetime.now()),
                        'return_date': self.__get_return_date(datetime.now())
                    }
                    borrow['user'].agregar_prestamo(borrow_vals)
