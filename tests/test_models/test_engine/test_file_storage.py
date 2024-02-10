import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test cases for FileStorage class
    """

    def setUp(self):
        """Set up method"""
        self.test_file_path = "file.json"

        self.storage = FileStorage()


    def tearDown(self):
        """Teardown method"""

        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_is_instance_of_FileStorage(self):
        """test if storage is instance of FileStorage"""

        self.assertIsInstance(self.storage, FileStorage)

    def test_initializatuon(self):
        """Test if storage is properly initialized"""

        self.assertEqual(self.storage.file_path, self.test_file_path)
        self.assertEqual(self.storage.objects, {})
        self.assertIsInstance(self.storage.objects, dict)

    def test_all_method(self):
        """Test for all method"""
        pass

    def test_new_method(self):
        """Test for new method"""
        pass

    def test_save_method(self):
        """Test for save method"""
        pass
    
    def test_reload_method(self):
        """Test for reload method"""
        pass

if __name__ == '__main__':
    unittest.main()
