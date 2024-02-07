from models.base_models import BaseModel
import unittest

class TestBaseModel(unittest.TestCase):
    """
    This test case contain tests for BaseModel class
    """
    def setUp(self):
        """This method sets the test fixture"""
        self.base_1 = BaseModel()
        self.base_2 = BaseModel()

    def test_instance_of_BaseModel(self):
        """
        Test if object is instance of BaseModel
        """
        self.assertIsInstance(base_1, BaseModel, "Must be an instance of BaseModel")

        self.assertIsInstance(base_2, BaseModel, "Must be an instance of BaseModel")

    def test_id_creation(self):
        """Test if instance has id attribute"""

        self.assertTrue(hasattr(base_1, 'id'), "id attribute should be created")
        self.assertTrue(hasattr(base_2, 'id'), "id attribute should be created")

    def test_id_is_string(self):
        """Test if id is a string"""

        self.assertIsInstance(base_1.id, str, "id should be a string")

    def test_created_at_creation(self):
        """Test if instance has created_at attribute"""

        self.assertTrue(hasattr(base_1, 'created_at'), "created_at attribute should be created")
        self.assertTrue(hasattr(base_2, 'created_at'), "created_at attribute should be created")

    def test_unique_ids(self):
        """Test if generated ids are unique"""

        self.assertNotEqual(base_1.id, base_2.id, "ids must be different")

    def test_unique_created_at(self):
        """Test if generated created_at are unique"""

        self.assertNotEqual(base_1.created_at, base_2.created_at, "created datetime must be different")