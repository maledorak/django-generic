from django.test import TestCase

from django_generic.db_expressions import db_replace
from tests.factories import ExampleModelFactory
from tests.models import ExampleModel


class TestDbReplace(TestCase):
    def setUp(self):
        self.test_obj1 = ExampleModelFactory(name='value1')
        self.test_obj2 = ExampleModelFactory(name='value2')

    def test_db_replace(self):
        self.assertEqual(self.test_obj1.name, 'value1')
        self.assertEqual(self.test_obj2.name, 'value2')
        ExampleModel.objects.all().update(name=db_replace('name', 'value1', 'supervalue1'))
        self.test_obj1.refresh_from_db()
        self.test_obj2.refresh_from_db()
        self.assertEqual(self.test_obj1.name, 'supervalue1')
        self.assertEqual(self.test_obj2.name, 'value2')
