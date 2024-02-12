import unittest
from models.review import Review
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test cases for Review class
    """

    def setUp(self):
        """setup method for the test cases"""
        self.review = Review()

    def test_if_review_issubclass(self):
        """Test if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel),
                        "Review must be a subclass of BaseModel")

    def test_instance_of_review(self):
        """
        Test if review is instance of Review
        """
        self.assertIsInstance(self.review, Review,
                              "Must be an instance of Review")

    def test_place_id(self):
        """Test if Review has place_id attribute"""
        self.assertTrue(hasattr(self.review, 'place_id'))


if __name__ == "__main__":
    unittest.main()
