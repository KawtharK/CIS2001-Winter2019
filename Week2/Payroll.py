from enum import Enum
import copy

class Employee:

    def __init__(self):
        self._name = ""
        self._hours_worked = 0
        self._dollars_per_hour = 0
        self._manager = None

    def set_manager(self, manager):
        self._manager = manager

    def get_manager(self):
        return self._manager

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def add_hours_worked(self, hours_worked, payroll_pin):
        if self._manager == None:
            raise AttributeError("Employee must have a manager assigned")

        if self._manager.validate_pin(payroll_pin):
            self._hours_worked += hours_worked
        else:
            raise ValueError("invalid payroll pin")

    def get_hours_worked(self):
        return self._hours_worked

    def set_pay_rate(self, dollars_per_hour):
        self._dollars_per_hour = dollars_per_hour

    def get_pay_rate(self):
        return self._dollars_per_hour

    def pay(self):
        overtime = 0
        hours = self._hours_worked
        self._hours_worked = 0
        if hours > 40:
            overtime = hours - 40
        return hours \
            * self._dollars_per_hour \
            + self._dollars_per_hour * .5 * overtime

class Pay_Period(Enum):
    Weekly = 1,
    BiWeekly = 2,
    Monthly = 3

class Manager(Employee):

    def __init__(self):
        super().__init__()
        self._annual_salary = 0
        self._payroll_pin = 0

    def set_payroll_pin(self, payroll_pin):
        self._payroll_pin = payroll_pin

    def validate_pin(self, payroll_pin):
        return self._payroll_pin == payroll_pin

    def set_annual_salary(self, annual_salary):
        self._annual_salary = annual_salary

    def get_annual_salary(self):
        return self._annual_salary

    def pay(self, pay_period):
        divided_by = 0
        if pay_period == Pay_Period.Weekly:
            divided_by = 52
        elif pay_period == Pay_Period.BiWeekly:
            divided_by = 26
        elif pay_period == Pay_Period.Monthly:
            divided_by = 12
        else:
            raise ValueError("Please use a valid Pay Period")
        return self._annual_salary / divided_by

    def set_pay_rate(self, dollars_per_hour):
        raise TypeError("Managers don't have hourly pay rates")

    def add_hours_worked(self, hours_worked):
        raise TypeError("Managers hours worked are not tracked")