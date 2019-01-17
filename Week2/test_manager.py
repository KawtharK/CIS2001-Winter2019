from unittest import TestCase
import Payroll


class TestManager(TestCase):
    def test_set_annual_salary(self):
        # Arrange
        annual_salary = 90000

        # Act
        manager = Payroll.Manager()
        manager.set_annual_salary(annual_salary)

        # Assert
        self.assertEqual(annual_salary, manager.get_annual_salary())

    def test_pay(self):
        # Arrange
        annual_salary = 90000

        # Act
        manager = Payroll.Manager()
        manager.set_annual_salary(annual_salary)

        # Assert
        self.assertEqual(annual_salary / 52, manager.pay(Payroll.Pay_Period.Weekly))
        self.assertEqual(annual_salary / 26, manager.pay(Payroll.Pay_Period.BiWeekly))
        self.assertEqual(annual_salary / 12, manager.pay(Payroll.Pay_Period.Monthly))

    def test_set_pay_rate(self):
        with self.assertRaises(TypeError):
            # Arrange

            # Act
            manager = Payroll.Manager()
            manager.set_pay_rate(10)

            # Assert - see with block?

    def test_add_hours_worked(self):
        with self.assertRaises(TypeError):
            # Arrange

            # Act
            manager = Payroll.Manager()
            manager.add_hours_worked(10)

            # Assert - see with block?
