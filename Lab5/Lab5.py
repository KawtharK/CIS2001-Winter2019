from StackAndQueue import MyStack, CircularQueue
import random

"""
#Create a fast food simulator and see if you can optimize for max profit

Loop for 100 turns

each turn, there is a 1 in 3 chance a car drives up.

track the turn # the car arrives

the car in front of the line can order - they order 1-5 burgers and 1-5 fries randomly

the cook can have 4 orders of fries and 4 burgers cooking at once.  burgers take 3 minutes to make and fries take 2 minutes.

You can have up to 5 extra burgers ready to serve, but they expire after 5 minutes ( track the turn # they are done being cooked if they go into the burger chute ).  8 orders of fries fit in the warmer at a time, but they are stacked on top of each other, and fries older than 5 minutes are stale and can't be served.

Served burgers earn $1 and fries $.50

if a car has waited for more than 5 minutes, assume it drives off and the car behind it pulls up.
"""


class GoodBurger:

    TARGET_READY_FRIES = 1
    TARGET_READY_BURGERS = 2
    MAX_FRIES_COOKING = 4
    FRY_COOK_TIME = 2
    MAX_FRY_STACK_SIZE = 8
    EARNING_PER_FRY = .5
    TIMES_UNTIL_FRIES_ARE_GROSS = 5
    MINUTES_UNTIL_CAR_DRIVES_OFF = 10

    def __init__(self):
        self.grease_pit_to_cook_fries_in = CircularQueue()
        self.cooktop = CircularQueue()
        self.fry_stack = MyStack()
        self.burger_chute = CircularQueue()
        self.drive_thru = CircularQueue()
        self.money = 0
        self.turn_number = 0

    def __str__(self):
        return "Good Burger Report - Number of Turns: {} - Money Earned: ${}".format(self.turn_number, self.money)

    def simulate(self, turns):
        for turn in range(turns):
            self.turn_number = turn

            self.check_grease_pit_for_done_fries()

            # 1 in 3 chance a car gets added to the drive_thru
            self.does_car_showup()

            # take the order from the front car
            self.take_front_car_order()

            # cook more things
            self.get_to_ready_targets()

    def check_grease_pit_for_done_fries(self):
        while not self.grease_pit_to_cook_fries_in.is_empty() \
                and self.grease_pit_to_cook_fries_in.first() + GoodBurger.FRY_COOK_TIME <= self.turn_number:
            if len(self.fry_stack) < GoodBurger.MAX_FRY_STACK_SIZE:
                self.fry_stack.push(self.turn_number)
                self.grease_pit_to_cook_fries_in.dequeue()
            else:
                # fries burn, throw away
                self.money -= GoodBurger.EARNING_PER_FRY
                self.grease_pit_to_cook_fries_in.dequeue()

    def does_car_showup(self):
        if random.randint(1,3) == 1:
            self.drive_thru.enqueue(Car(self.turn_number))

    def take_front_car_order(self):
        if not self.drive_thru.is_empty():
            if self.drive_thru.first().time_arrived + GoodBurger.MINUTES_UNTIL_CAR_DRIVES_OFF > self.turn_number:
                if len(self.fry_stack) < self.drive_thru.first().number_of_fries_to_order:
                    while len(self.grease_pit_to_cook_fries_in) < GoodBurger.MAX_FRIES_COOKING \
                            and len(self.grease_pit_to_cook_fries_in) < self.drive_thru.first().number_of_fries_to_order:
                        self.grease_pit_to_cook_fries_in.enqueue(self.turn_number)
                else:
                    for fry in range(self.drive_thru.first().number_of_fries_to_order):
                        if self.fry_stack.peek() + GoodBurger.TIMES_UNTIL_FRIES_ARE_GROSS <= self.turn_number:
                            self.fry_stack.pop()
                            self.drive_thru.first().number_of_fries_served += 1
                            self.money += GoodBurger.EARNING_PER_FRY
                        else:
                            self.fry_stack.pop()
                            self.money -= GoodBurger.EARNING_PER_FRY
                if self.drive_thru.first().number_of_fries_to_order == self.drive_thru.first().number_of_fries_served:
                    self.drive_thru.dequeue()
            else:
                # car drives off and we lose money
                self.money -= self.drive_thru.first().number_of_fries_to_order * GoodBurger.EARNING_PER_FRY
                self.drive_thru.dequeue()

    def get_to_ready_targets(self):
        if len(self.fry_stack) < GoodBurger.TARGET_READY_FRIES:
            for fry in range(GoodBurger.TARGET_READY_FRIES - len(self.fry_stack)):
                if len(self.grease_pit_to_cook_fries_in) < GoodBurger.MAX_FRIES_COOKING:
                    self.grease_pit_to_cook_fries_in.enqueue(self.turn_number)


class Car:

    def __init__(self, time_arrived):
        self.time_arrived = time_arrived
        self.number_of_burgers_to_order = random.randint(1, 5)
        self.number_of_fries_to_order = random.randint(1, 5)
        self.number_of_fries_served = 0
        self.number_of_burgers_served = 0


fry_shop = GoodBurger()
fry_shop.simulate(20)
print(fry_shop)
