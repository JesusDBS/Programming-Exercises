from datetime import datetime
import random

class Reloj:
    instances = []
    n_instance = 0
    
    def __init__(self) -> None:
        self.__horas = random.randint(0, 23)
        self.__minutos = random.randint(0, 59)
        self.__segundos = random.randint(0, 59)

        self.__class__.instances.append(self)

        if len(self.instances) > 1:
            self.__class__.n_instance += 1
            self.__id = self.__class__.n_instance
        
        else:
            self.__id = self.__class__.n_instance

    @property
    def id(self):
        return self.__id

    @property
    def horas(self):
        return self.__horas
    
    @horas.setter
    def horas(self, value: int) -> int: 
        if isinstance(value, int):
            if value >= 0 and value <= 23:
                self.__horas = value
                return self.__horas
            
            raise ValueError(f'horas: {value} must be between 0 and 23')
        raise TypeError(f'horas: {value} must be an integer!')
    
    @property
    def minutos(self):
        return self.__minutos
    
    @minutos.setter
    def minutos(self, value: int) -> int:
        if isinstance(value, int):
            if value >= 0 and value <= 59:
                self.__minutos = value
                return self.__minutos
            
            raise ValueError(f'minutos: {value} must be between 0 and 59')
        raise TypeError(f'minutos: {value} must be an integer!')
    
    @property
    def segundos(self):
        return self.__segundos
    
    @segundos.setter
    def segundos(self, value: int) -> int:
        if isinstance(value, int):
            if value >= 0 and value <= 59:
                self.__segundos = value
                return self.__segundos
            
            raise ValueError(f'segundos: {value} must be between 0 and 59')
        raise TypeError(f'segundos: {value} must be an integer!')
    
    def agregar_horas(self, horas: int) -> None:
        self.horas = horas

    def agregar_minutos(self, minutos: int) -> None:
        self.minutos = minutos

    def agregar_segundos(self, segundos: int) -> None:
        self.segundos = segundos
    
    def create_new_alarm(self, horas: int, minutos: int = 0, segundos: int = 0) -> None:
        self.agregar_horas(horas)
        self.agregar_minutos(minutos)
        self.agregar_segundos(segundos)

    @staticmethod
    def get_current_time() -> str:
        format = "%H:%M:%S"

        print(datetime.now().strftime(format))
    
    def __str__(self) -> str:
        return f"{self.id} - {self.__class__.__name__} horas: {self.horas}, minutos: {self.minutos}, segundos: {self.segundos}"
    
    @classmethod
    def display_alarms(cls):
        if cls.instances:
            for alarm in cls.instances:
                print(alarm)
                

        else:
            print("There is no alarms!")

    @classmethod
    def delete_alarm(cls, id: int):
        del cls.instances[id]

    @classmethod
    def get_alarm_by_id(cls, id: int):
        alarm = list(filter(lambda reloj: reloj.id == id, cls.instances))[0]

        if not alarm:
            return False

        return alarm