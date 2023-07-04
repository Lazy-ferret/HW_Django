from unittest import TestCase
from rest_framework.test import APIClient


class TestSampleView(TestCase):
    def test_view_200(self):
        url = '/api/v1/'
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
