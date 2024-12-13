from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class BuyOrderAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_buy_order(self):
        data = {
            "currency_name": "bitcoin",
            "num_of_cryptos": 5
        }
        response = self.client.post('/api/buyorder/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)