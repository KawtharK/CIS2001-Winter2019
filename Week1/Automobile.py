class Automobile:
    def __init__(self, gas_capacity_in_gallons):
        self._gas_capacity_in_gallons = gas_capacity_in_gallons
        self._gas_in_tank_in_gallons = 0

    def add_gas(self, gallons):
        if self._gas_in_tank_in_gallons + gallons > self._gas_capacity_in_gallons:
            raise ValueError("You can't put that much gas in!")

        self._gas_in_tank_in_gallons += gallons



if __name__ == '__main__':
    car = Automobile(10)

    print(car)
    print(car._gas_capacity_in_gallons)
    print("Gas in tank before: ", car._gas_in_tank_in_gallons)
    car.add_gas(10)
    print("Gas in tank after: ", car._gas_in_tank_in_gallons)


