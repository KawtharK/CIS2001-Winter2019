from unittest import TestCase
import Automobile

class TestAutomobile(TestCase):
    def test_init(self):
        # AAA method for unit tests

        # Arrange
        gas_capacity = 10
        expected_gallons_in_tank = 0

        # Act
        car = Automobile.Automobile(gas_capacity)

        # Assert
        self.assertEqual(expected_gallons_in_tank, car._gas_in_tank_in_gallons)
        self.assertEqual(gas_capacity, car._gas_capacity_in_gallons)

    def test_add_gas(self):
        car = Automobile.Automobile(10)
        car.add_gas(10)
        self.assertEqual(10, car._gas_in_tank_in_gallons)

        with self.assertRaises(ValueError):
            car.add_gas(10)
