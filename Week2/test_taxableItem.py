from unittest import TestCase
import Item

class TestTaxableItem(TestCase):

    def test_TaxableItem_Init_Tax_Rate_1_Point_06(self):

        # Arrange
        item_name = "cake"
        item_price = 4.0
        tax_rate = 1.06
        expected_tax_rate = tax_rate - 1

        # Act
        taxable_item = Item.TaxableItem(item_name, item_price, tax_rate)

        # Assert
        self.assertEqual(item_name, taxable_item._name)
        self.assertEqual(item_price, taxable_item._price)
        self.assertEqual(expected_tax_rate, taxable_item._tax_rate)

    def test_TaxableItem_Init_Tax_Rate_6(self):
        # Arrange
        item_name = "cake"
        item_price = 4.0
        tax_rate = 6
        expected_tax_rate = tax_rate / 100

        # Act
        taxable_item = Item.TaxableItem(item_name, item_price, tax_rate)

        # Assert
        self.assertEqual(item_name, taxable_item._name)
        self.assertEqual(item_price, taxable_item._price)
        self.assertEqual(expected_tax_rate, taxable_item._tax_rate)

    def test_TaxableItem_Init_Tax_Rate_Point_06(self):
        # Arrange
        item_name = "cake"
        item_price = 4.0
        tax_rate = .06
        expected_tax_rate = tax_rate

        # Act
        taxable_item = Item.TaxableItem(item_name, item_price, tax_rate)

        # Assert
        self.assertEqual(item_name, taxable_item._name)
        self.assertEqual(item_price, taxable_item._price)
        self.assertEqual(expected_tax_rate, taxable_item._tax_rate)

    def test_get_purchase_price(self):
        # Arrange
        item_name = "cake"
        item_price = 4.0
        tax_rate = .06
        expected_tax_rate = tax_rate

        # Act
        taxable_item = Item.TaxableItem(item_name, item_price, tax_rate)

        # Assert
        self.assertEqual(item_price * tax_rate + item_price, \
                         taxable_item.get_purchase_price())
