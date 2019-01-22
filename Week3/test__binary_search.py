from unittest import TestCase
import Week3

class Test_binary_search(TestCase):
    def test_binary_search_found_item(self):
        # Arrange
        numbers = [42, 16, 21, 9, 81, 7, 2]
        numbers.sort()

        # Act
        result = Week3.binary_search_iterative(numbers,42)

        # Assert
        self.assertTrue(result)

    def test_binary_search_found_item_highest(self):
        # Arrange
        numbers = [42, 16, 21, 9, 81, 7, 2]
        numbers.sort()

        # Act
        result = Week3.binary_search_iterative(numbers, 81)

        # Assert
        self.assertTrue(result)

    def test_binary_search_found_item_lowest(self):
        # Arrange
        numbers = [42, 16, 21, 9, 81, 7, 2]
        numbers.sort()

        # Act
        result = Week3.binary_search_iterative(numbers, 2)

        # Assert
        self.assertTrue(result)

    def test_binary_search_not_found(self):
        # Arrange
        numbers = [42, 16, 21, 9, 81, 7, 2]
        numbers.sort()

        # Act
        result = Week3.binary_search_iterative(numbers, 1)

        # Assert
        self.assertFalse(result)