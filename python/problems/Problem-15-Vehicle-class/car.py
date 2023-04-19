from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand:str, model:str, license_plate:str, **kwargs) -> None:
        super().__init__(**kwargs)

        self.__brand = brand
        self.__model = model
        self.__license_plate = license_plate
        self.capacity = 4

    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, value):
        if isinstance(value, str):
            self.__brand = value
            return self.__brand
        raise ValueError(f'Value: {value} must be a string')
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        if isinstance(value, str):
            self.__model = value
            return self.__model
        raise ValueError(f'Value: {value} must be a string')

    
    @property
    def license_plate(self):
        return self.__license_plate
    
    @license_plate.setter
    def license_plate(self, value):
        if isinstance(value, str):
            self.__license_plate = value
            return self.__license_plate
        raise ValueError(f'Value: {value} must be a string')