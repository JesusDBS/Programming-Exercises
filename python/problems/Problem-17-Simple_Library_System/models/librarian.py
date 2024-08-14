from .user import User


class Librarian(User):
    def __init__(self, nombre: str, apellido: str, dni: int) -> None:
        super().__init__(nombre, apellido, dni)
        self.activo = True
