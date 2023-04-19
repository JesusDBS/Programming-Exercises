import io
import unittest
import unittest.mock
from vehicle import Vehicle
from bus import Bus
from car import Car


class TestVehicleClass(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(name='vehicle', max_speed=100, milage=120000)
        return super().setUp()
    
    def tearDown(self) -> None:
        del self.vehicle
        return super().tearDown()
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, output, mock_stdout):
        print(self.vehicle)
        self.assertEqual(mock_stdout.getvalue(), output)
    
    def test_if_max_speed_exists(self):
        self.assertTrue(hasattr(self.vehicle, 'max_speed'))

    def test_if_milage_exists(self):
        self.assertTrue(hasattr(self.vehicle, 'milage'))

    def test_name_exists(self):
        self.assertTrue(hasattr(self.vehicle, 'name'))

    def test_str(self):
        message = f'Color: white, Vehicle Name: vehicle, Speed: 100, Milage: 120000\n'
        self.assert_stdout(message)

    def test_vehicle_has_capacity_attr(self):
        self.assertTrue(hasattr(self.vehicle, 'capacity'))

    def test_calculate_fare(self):
        self.assertEqual(self.vehicle.calculate_fare(), 100)

class TestBusClass(unittest.TestCase):
    def setUp(self) -> None:
        self.bus = Bus(name='School Volvo', max_speed=180, milage=12)
        return super().setUp()
    
    def tearDown(self) -> None:
        del self.bus
        return super().tearDown()
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, instance, output, mock_stdout):
        print(instance)
        self.assertEqual(mock_stdout.getvalue(), output)
    
    def test_bus_is_child_of_vehicle(self):
        self.assertTrue(isinstance(self.bus, Vehicle))

    def test_bus_str(self):
        message = "Color: white, Bus Name: School Volvo, Speed: 180, Milage: 12\n"
        self.assert_stdout(self.bus, message)
    
    def test_bus_has_capacity_attr(self):
        self.assertTrue(hasattr(self.bus, 'capacity'))

    def test_bus_seatig_capacity(self):
        message = "The seating capacity of a School Volvo is 50 passengers\n"
        self.assert_stdout(self.bus.seating_capacity(), message)

    def test_calculate_fare(self):
        self.assertEqual(self.bus.calculate_fare(), 5500)

class TestCarClass(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car(name="Aveo", brand="Chevrolet", license_plate="1998Ve", model="aveo hb")
        
        return super().setUp()
    
    def tearDown(self) -> None:
        del self.car
        return super().tearDown()
    
    def test_car_is_child_of_vehicle(self):
        self.assertTrue(isinstance(self.car, Vehicle))

    def test_car_has_bran_attr(self):
        self.assertTrue(hasattr(self.car, 'brand'))

    def test_car_has_model_attr(self):
        self.assertTrue(hasattr(self.car, 'model'))

    def test_car_has_license_plate_attr(self):
        self.assertTrue(hasattr(self.car, 'license_plate'))

    def test_car_capacity(self):
        self.assertEqual(self.car.capacity, 4)

    def test_calculate_fare(self):
        self.assertEqual(self.car.calculate_fare(), 400)


if __name__ == "__main__":
    unittest.main()