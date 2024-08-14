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
