from datetime import datetime, timedelta
from .user import User


class Book:

    def __init__(self,
                 titulo: str,
                 categoria: str,
                 autor: str,
                 idioma: str,
                 unidades: int,
                 ) -> None:
        assert isinstance(titulo, str), f"EL TITULO DEBE SER UN STRING!"
        assert isinstance(categoria, str), f"LA CATEGORIA DEBE SER UN STRING!"
        assert isinstance(autor, str), f"EL AUTOR DEBE SER UN STRING!"
        assert isinstance(idioma, str), f"EL IDIOMA DEBE SER UN STRING!"
        assert isinstance(unidades, int), f"LAS UNIDADES DEBEN SER UN ENTERO!"
        assert unidades > 0, f"LAS UNIDADES DEBEN SER MAYORES A CERO!"

        self.titulo = titulo
        self.categoria = categoria
        self.autor = autor
        self.idioma = idioma
        self.__unidades = unidades
        self.__uni_disponibles = unidades
        self.__prestamos = []

    @property
    def prestamos(self):
        return self.__prestamos

    @property
    def unidades(self):
        return self.__unidades

    def __str__(self) -> str:
        return f"{self.titulo} ({self.autor})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.titulo}, {self.categoria}, {self.autor}, {self.idioma}, {self.unidades})"

    @unidades.setter
    def unidades(self, unidades: int):
        if isinstance(unidades, int):
            self.__unidades = unidades
        raise TypeError('LAS UNIDADES DEBEN SER NÚMEROS ENTEROS.')

    def update_unidades(self, unidades: int):
        self.unidades = unidades

    @property
    def unidades_disponibles(self):
        return self.__uni_disponibles

    @unidades_disponibles.setter
    def unidades_disponibles(self, unidades: int):
        if isinstance(unidades, int):
            self.__uni_disponibles = unidades
        raise TypeError('LAS UNIDADES DEBEN SER NÚMEROS ENTEROS.')

    def update_unidades_disponibles(self, unidades):
        self.unidades_disponibles = unidades

    def __agregar_prestamo(self, data: dict):
        data_values = ['user', 'borrow_date', 'retun_date']
        if data and isinstance(data, dict):
            for value in data_values:
                if value not in data.keys():
                    raise Exception(
                        'LA DATA DE PRESTAMO DEBE CONTENER LOS SIGUIENTES ELEMENTOS: {}'.format(data_values))

            for prestamo in self.prestamos:
                if data['user'] == prestamo['user']:
                    raise Exception(
                        f'El USUARIO {data['user'].name} YA TIENE UN PRESTAMO DE ESTE LIBRO!'
                    )

            self.prestamos.append(data)

    def __eliminar_prestamo(self, user: User):
        if isinstance(user, User):
            for prestamo in self.prestamos:
                if user == prestamo['user']:
                    self.prestamos.remove(prestamo)

        raise Exception(
            'DEBE ENVIAR UN USUARIO PARA ELIMINAR SU PRESTAMO!')

    @staticmethod
    def __date_2_string(date: datetime, format: str = '%d/%m/%Y') -> str:
        return date.strftime(format)

    def __get_return_date(self, date: datetime, days: int = 3, format: str = '%d/%m/%Y') -> str:
        return_date = date + timedelta(days=days)
        return self.__date_2_string(return_date, format=format)

    def prestar_libro(self, user: User):
        if self.unidades_disponibles > 1:
            self.__agregar_prestamo({
                'user': user,
                'borrow_date': self.__date_2_string(datetime.now()),
                'return_date': self.__get_return_date(datetime.now())
            })
            self.unidades_disponibles -= 1
        raise Exception(
            f'LAS UNDIADES DEL LIBRO "{self.titulo}" SE HAN AGOTADO. SOLO ESTA DISPONIBLE EL EJEMPLAR DE SALA.')

    def devolver_libro(self, user: User):
        if self.unidades_disponibles == self.unidades:
            self.__eliminar_prestamo(user)
            self.unidades_disponibles += 1
        raise Exception(
            f'EL LIBRO "{self.titulo}" NO TIENE PRESTAMOS ACTIVOS.')

    def mostrar_disponibilidad(self):
        message = f'Se encuentan {self.unidades_disponibles} de este libro {self.titulo}.'
        print(message)

    def mostrar_datos(self):
        print(self)

    def listar_prestamos(self):
        if not self.prestamos:
            raise Exception('ESTE LIBRO NO TIENE PRESTAMOS')

        print(f'Prestamnos del libro {self.titulo}: ', '\n')
        for numero, prestamo in enumerate(self.prestamos):
            numero += 1
            print(f'{numero}) {prestamo['user'].name} - {prestamo['borrow_date']} - {prestamo['return_date']}')
