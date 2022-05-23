#Polygon Area:
# Create ONE FUNCTION (it is important that it is only one) that is able to calculate and return the area of a polygon.
#  - The function will receive by parameter only ONE polygon at a time.
#  - The supported polygons will be Triangle, Square and Rectangle.
#  - Prints the calculation of the area of one polygon of each type.

class Polygon:

    def __init__(self, nl: int, b: float, h: float):

        #validations
        assert isinstance(nl,int), f'The number of sides must be an integer! You entered {nl}'
        assert nl > 0, f'The number of sides {nl} must be greater than zero!'
        assert nl <= 4, f'The supported polygons are Triangle, Square and Rectagle. You entered a polygong with {nl} sides.'
        assert b > 0, f'Base of Polygon {b} must be greater than zero!'
        assert h > 0, f'Height of Polygon {h} must be greater than zero!'

        self.nl = nl
        self.b = b
        self.h = h
    
    @property
    def polygon_name(self):
        if self.nl == 3:
            return "Triangle"

        if self.nl == 4:
            if self.b == self.h:
                return "Square"
            else:
                return "Rectangle"

    @property
    def polygon_area(self):
        if self.nl == 3:
            return self.b*self.h/2

        if self.nl == 4:
            if self.b == self.h:
                return self.b**2
            
            else:
                return self.b*self.h


def main():

    nl = int(input('Enter the polygon sides: '))
    b = int(input('Enter the base of the polygon: '))
    h = int(input('Enter the height of the polygon: '))

    polygon = Polygon(nl,b,h)

    messure = input('Enter the messure of polygon sides: ')

    print(f'The Polygon is a {polygon.polygon_name} and its area is {polygon.polygon_area} {messure}^2.')

if __name__ == "__main__":
    main()

    

    