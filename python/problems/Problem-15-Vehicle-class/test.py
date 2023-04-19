import io
import unittest
import unittest.mock
from vehicle import Vehicle
from bus import Bus


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
        message = "Color: white, Vehicle Name: School Volvo, Speed: 180, Milage: 12\n"
        self.assert_stdout(self.bus, message)
    
    def test_bus_has_capacity_attr(self):
        self.assertTrue(hasattr(self.bus, 'capacity'))

    def test_bus_seatig_capacity(self):
        message = "The seating capacity of a School Volvo is 50 passengers\n"
        self.assert_stdout(self.bus.seating_capacity(), message)


if __name__ == "__main__":
    unittest.main()