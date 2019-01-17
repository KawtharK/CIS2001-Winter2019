from unittest import TestCase
import Payroll


class TestEmployee(TestCase):

    def test_init(self):
        # AAA

        # Arrange

        # Act
        employee = Payroll.Employee()

        # Assert
        self.assertEqual("", employee.get_name())
        self.assertEqual(0, employee.get_pay_rate())
        self.assertEqual(0, employee.get_hours_worked())

    def test_set_name(self):
        # AAA

        # Arrange
        name = "Eric"

        # Act
        employee = Payroll.Employee()
        employee.set_name(name)

        # Assert
        self.assertEqual(name, employee.get_name())

    def test_add_hours_worked(self):
        pass
        # AAA

        # Arrange
        hours_worked = 60
        payroll_pin = 1234
        manager = Payroll.Manager()
        manager.set_payroll_pin(payroll_pin)

        # Act
        employee = Payroll.Employee()
        employee.set_manager(manager)
        employee.add_hours_worked(60, payroll_pin)

        # Assert
        self.assertEqual(hours_worked, employee.get_hours_worked())

    def test_set_pay_rate(self):
        pass
        # AAA

        # Arrange
        pay_rate = 40

        # Act
        employee = Payroll.Employee()
        employee.set_pay_rate(pay_rate)

        # Assert
        self.assertEqual(pay_rate, employee.get_pay_rate())

    def test_pay_with_overtime(self):
        pass
        # AAA

        # Arrange
        pay_rate = 40
        hours_worked = 60
        payroll_pin = 1234
        manager = Payroll.Manager()
        manager.set_payroll_pin(payroll_pin)

        # Act
        employee = Payroll.Employee()
        employee.set_pay_rate(pay_rate)
        employee.set_manager(manager)
        employee.add_hours_worked(hours_worked, payroll_pin)

        # Assert
        self.assertEqual(pay_rate * hours_worked \
                         + pay_rate * .5 * (hours_worked - 40), employee.pay())
        self.assertEqual(0, employee.get_hours_worked())

    def test_pay_without_overtime(self):
        pass
        # AAA

        # Arrange
        pay_rate = 40
        hours_worked = 20
        payroll_pin = 1234
        manager = Payroll.Manager()
        manager.set_payroll_pin(payroll_pin)

        # Act
        employee = Payroll.Employee()
        employee.set_pay_rate(pay_rate)
        employee.set_manager(manager)
        employee.add_hours_worked(hours_worked, payroll_pin)

        # Assert
        self.assertEqual(pay_rate * hours_worked, employee.pay())
        self.assertEqual(0, employee.get_hours_worked())


    def test_set_manager(self):
        # Arrange
        manager = Payroll.Manager()

        # Act
        employee = Payroll.Employee()
        employee.set_manager(manager)

        # Assert
        self.assertEqual(manager, employee.get_manager())


