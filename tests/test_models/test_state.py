import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test cases for User class
    """

    def setUp(self):
        """setup method for the test cases"""
        self.state1 = State()

    def test_if_state_issubclass(self):
        """Test if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(State, BaseModel),
                        "State must be a subclass of BaseModel")

    def test_instance_of_State(self):
        """
        Test if state1 is instance of State
        """
        self.assertIsInstance(self.state1, State,
                              "Must be an instance of State")

    def test_name(self):
        """Test if State has name attribute"""
        self.assertTrue(hasattr(self.state1, 'name'))


if __name__ == "__main__":
    unittest.main()
