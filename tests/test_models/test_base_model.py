#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
import pep8
import json
import os


class test_basemodel(unittest.TestCase):
    """Tests BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Creates an instance"""

        cls.base_model = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """Deletes the created instance"""

        del cls.base_model

    def tearDown(self):
        """Removes file.json after every test"""

        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_documentation(self):
        """Tests if the module, the class,
        and the methods are documented"""

        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_following_pep8(self):
        """Tests if the code follows pep8 style guide"""

        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/base_model.py'])

        self.assertEqual(result.total_errors, 0, 'Found style errors.')

    def test_hasattr(self):
        """Tests if methods exist"""

        self.assertTrue(hasattr(BaseModel, '__init__'))
        self.assertTrue(hasattr(BaseModel, '__str__'))
        self.assertTrue(hasattr(BaseModel, 'save'))
        self.assertTrue(hasattr(BaseModel, 'to_dict'))
        self.assertTrue(hasattr(BaseModel, 'delete'))

    def test_isinstance(self):
        """Tests instantiation"""

        self.assertTrue(isinstance(self.base_model, BaseModel))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     'Database storage is being used.')
    def test_save(self):
        """Tests save method"""

        self.base_model.save()
        self.assertNotEqual(
            self.base_model.created_at,
            self.base_model.updated_at)

    def test_to_dict(self):
        """Tests to_dict method"""

        dict = self.base_model.to_dict()

        self.assertIsInstance(dict['created_at'], str)
        self.assertIsInstance(dict['updated_at'], str)
        self.assertEqual(self.base_model.__class__.__name__, 'BaseModel')

    # Additional Tests
    def test_default(self):
        """Tests the default constructor"""
        instance = BaseModel()
        self.assertEqual(type(instance), BaseModel)

    def test_kwargs(self):
        """Tests the constructor with keyword arguments"""
        instance = BaseModel()
        copy = instance.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is instance)

    def test_kwargs_int(self):
        """Tests the constructor with invalid keyword arguments"""
        instance = BaseModel()
        copy = instance.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save_additional(self):
        """Tests the save method for additional functionality"""
        instance = BaseModel()
        instance.save()
        key = 'BaseModel.' + instance.id
        with open('file.json', 'r') as f:
            data = json.load(f)
            self.assertEqual(data[key], instance.to_dict())

    def test_str_additional(self):
        """Tests the __str__ method for additional functionality"""
        instance = BaseModel()
        expected_output = '[BaseModel] ({}) {}'.format(instance.id,
                                                       instance.__dict__)
        self.assertEqual(str(instance), expected_output)


if __name__ == "__main__":
    unittest.main()
