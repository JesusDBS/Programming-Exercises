from vehicle import Vehicle

class Bus(Vehicle):
    """
    Simple bus class
    """
    def __init__(self, name:str, capacity:int=50, max_speed:int=0, milage:int=0) -> None:
        super().__init__(name=name, capacity=capacity, max_speed=max_speed, milage=milage)
    