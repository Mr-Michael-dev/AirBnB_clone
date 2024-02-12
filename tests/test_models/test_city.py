import unittest
from models.city import City
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test cases for City class
    """

    def setUp(self):
        """setup method for the test cases"""
        self.city1 = City()

    def test_if_city_issubclass(self):
        """Test if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel),
                        "City must be a subclass of BaseModel")

    def test_instance_of_City(self):
        """
        Test if city1 is instance of State
        """
        self.assertIsInstance(self.city1, City,
                              "Must be an instance of City")

    def test_name(self):
        """Test if City has state_id attribute"""
        self.assertTrue(hasattr(self.city1, "state_id"))

    def test_name(self):
        """Test if City has name attribute"""
        self.assertTrue(hasattr(self.city1, "name"))


if __name__ == "__main__":
    unittest.main()
