# ---------------------------------------------------
# Vehicle Class:
# 1) Write a Python program to create a Vehicle class with max_speed and mileage instance attributes
# 2) Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# 3) Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
# 4) Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. 
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

# ---------------------------------------------------

class Vehicle:
    """
    Simple vehicle class
    """
    color = "white"

    def __init__(self, name:str, capacity:int=1, max_speed:int=0, milage:int=0) -> None:
        
        #validations
        assert isinstance(name, str), f'Name: {name} must be a string!'
        assert isinstance(max_speed, (int, float)), f'Max Speed:{max_speed} must be a Number data type!'
        assert isinstance(milage, (int, float)), f'Milage:{milage} must be a Number data type!'
        assert max_speed > 0, f'Max Speed:{max_speed} must be a greater than zero!'
        assert milage >= 0, f'Milage {milage} must be greater or equial than zero'

        #asignments
        self.name = name
        self.max_speed = max_speed
        self.milage = milage
        self.capacity = capacity

    def __str__(self) -> str:
        return f"Color: {self.color}, Vehicle Name: {self.name}, Speed: {self.max_speed}, Milage: {self.milage}"
    
    def seating_capacity(self):
        return f"The seating capacity of a {self.name} is {self.capacity} passengers"
    
    def calculate_fare(self):
        return self.capacity * 100

    