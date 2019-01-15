from unittest import TestCase
import Item

class TestItem(TestCase):

    def test_Item_init(self):
        # Arrange
        item_name = "cake"
        item_price = 4.0

        # Act
        item = Item.Item(item_name, item_price)

        # Assert
        self.assertEqual(item_price, item._price)
        self.assertEqual(item_name, item._name)

    def test_get_purchase_price(self):
        # AAA method for testing

        # Arrange
        item_name = "cake"
        item_price = 4.0

        # Act
        item = Item.Item(item_name, item_price)

        # Assert
        self.assertEqual(item_price, item.get_purchase_price())