import unittest

from django_generic.utils import get_class_from_path, md5_from_string


class TestGetClassFromPath(unittest.TestCase):
    def test_get_class_from_path(self):
        testing_path = '.'.join((self.__module__, self.__class__.__name__))
        generated_class = get_class_from_path(testing_path)
        self.assertEqual(generated_class, self.__class__)

    def test_get_class_from_string_when_string_is_not_path(self):
        testing_path = 'fakepath'
        self.assertRaises(TypeError, get_class_from_path, cls_str=testing_path)


class TestMd5FromString(unittest.TestCase):
    def test_md5_from_string(self):
        test_string = 'Some string'
        test_string_md5 = md5_from_string(test_string)
        expected_string = '80f855e731cc0c9aa336ca4d25f990be'
        self.assertEqual(test_string_md5, expected_string)
