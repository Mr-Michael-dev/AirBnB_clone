import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test cases for Amenity class
    """

    def setUp(self):
        """setup method for the test cases"""
        self.ame1 = Amenity()

    def test_if_amenity_issubclass(self):
        """Test if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel),
                        "Amenity must be a subclass of BaseModel")

    def test_instance_of_amenity(self):
        """
        Test if ame1 is instance of Amenity
        """
        self.assertIsInstance(self.ame1, Amenity,
                              "Must be an instance of Amenity")

    def test_name(self):
        """Test if Amenity has name attribute"""
        self.assertTrue(hasattr(self.ame1, 'name'))


if __name__ == "__main__":
    unittest.main()
