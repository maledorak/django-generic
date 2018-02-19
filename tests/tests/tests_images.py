import requests_mock
import unittest

from django_generic.images import get_image_from_url
from django_generic.mixins import MockFilesMixin


class TestGetImageFromUrl(MockFilesMixin, unittest.TestCase):
    @requests_mock.mock()
    def test_get_image_from_url(self, req_mock):
        image = self.generate_image(filename='supercat.png')
        req_mock.get(requests_mock.ANY, content=image.file.read(), headers={'Content-Type': 'image/jpeg'})
        image_from_url = get_image_from_url('https://supercat.com/supercat.png')
        self.assertEqual(image.size, image_from_url.size)
