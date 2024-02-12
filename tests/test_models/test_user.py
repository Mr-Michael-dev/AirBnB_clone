import unittest
from models.user import User
from models.base_model import BaseModel


class TestUserInheritance(unittest.TestCase):
    """Test user inheritance"""

    def test_if_user_issubclass(self):
        """Test if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(User, BaseModel),
                        "User must be a subclass of BaseModel")


class TestUser(unittest.TestCase):
    """
    Test cases for User class
    """

    def setUp(self):
        """setup method for the test cases"""
        self.user1 = User()

    def test_instance_of_User(self):
        """
        Test if user1 is instance of User
        """
        self.assertIsInstance(self.user1, User,
                              "Must be an instance of User")

    def test_email(self):
        """Test if User has email attribute"""
        self.assertTrue(hasattr(self.user1, 'email'))

    def test_password(self):
        """Test if User has password attribute"""
        self.assertTrue(hasattr(self.user1, 'password'))

    def test_first_name(self):
        """Test if User has first_namw attribute"""
        self.assertTrue(hasattr(self.user1, 'first_name'))

    def test_last_name(self):
        """Test if User has last_name attribute"""
        self.assertTrue(hasattr(self.user1, 'last_name'))


if __name__ == "__main__":
    unittest.main()
