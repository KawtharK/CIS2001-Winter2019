#import Automobile

# to not have to use the module name
from Automobile import Automobile, Truck

car = Automobile(10)

car.add_gas(5)

print(car)

semi = Truck(50, "CDL")
print(semi.can_drive("CDL"))