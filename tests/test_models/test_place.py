import unittest
from models.place import Place
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test cases for Place class
    """

    def setUp(self):
        """setup method for the test cases"""
        self.place1 = Place()

    def test_if_place_issubclass(self):
        """Test if Place is a subclass of BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel),
                        "Place must be a subclass of BaseModel")

    def test_instance_of_place(self):
        """
        Test if place1 is instance of Place
        """
        self.assertIsInstance(self.place1, Place,
                              "Must be an instance of Place")

    def test_name(self):
        """Test if Place has name attribute"""
        self.assertTrue(hasattr(self.place1, 'name'))


if __name__ == "__main__":
    unittest.main()
