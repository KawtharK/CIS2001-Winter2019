from unittest import TestCase
import ExampleProject

class TestThisDoesSomething(TestCase):
    def test_something(self):
        # AAA

        # Arrange

        #Act
        example = ExampleProject.ThisDoesSomething()
        result = example.something()

        #Assert
        self.assertEqual(result, 10)


    def test_otherthing(self):
        self.fail()

    def test_lastthing(self):
        self.fail()
