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

    def prestar_libro(self, user: User):
        # TODO Agregar diccionario con las llaves de usaurio, fecha de prestamo y devolución
        # y agregar diccionario a la lista de prestamos del libro
        # TODO Validar que la longitud de prestamnos no sea mayor a cantidad disponible

        if self.unidades_disponibles > 1:
            self.unidades_disponibles = self.unidades - 1
        raise Exception(
            f'LAS UNDIADES DEL LIBRO "{self.titulo}" SE HAN AGOTADO. SOLO ESTA DISPONIBLE EL EJEMPLAR DE SALA.')

    def devolver_libro(self):
        ...

    def mostrar_disponibilidad(self):
        ...

    def mostrar_datos(self):
        ...

    def listar_prestamos(self):
        ...
