class Automobile:
    def __init__(self, gas_capacity_in_gallons):
        self._gas_capacity_in_gallons = gas_capacity_in_gallons
        self._gas_in_tank_in_gallons = 0

    def add_gas(self, gallons):
        if self._gas_in_tank_in_gallons + gallons > self._gas_capacity_in_gallons:
            raise ValueError("You can't put that much gas in!")

        self._gas_in_tank_in_gallons += gallons

    def __str__(self):
        return "Automobile with {} gallon gas tank with {} gallons in the tank" \
            .format(self._gas_capacity_in_gallons, self._gas_in_tank_in_gallons)




class Truck(Automobile):
    def __init__(self, gas_capacity_in_gallons, endorsement_requirements):
        Automobile.__init__(self, gas_capacity_in_gallons)
        self.endorsement_requirements = endorsement_requirements

    def can_drive(self, drivers_license_endorsement):
        return drivers_license_endorsement == self.endorsement_requirements


if __name__ == '__main__':
    car = Automobile(10)

    print(car)
    print(car._gas_capacity_in_gallons)
    print("Gas in tank before: ", car._gas_in_tank_in_gallons)
    car.add_gas(10)
    print("Gas in tank after: ", car._gas_in_tank_in_gallons)


