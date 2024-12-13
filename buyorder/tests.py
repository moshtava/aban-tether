from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Crypto, Price, PricePerRial
from .views import BuyOrderView
from unittest.mock import patch

class BuyOrderAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.crypto = Crypto.objects.create(name='bitcoin', symbol='BTC')
        self.price = Price.objects.create(crypto=self.crypto, price_per_dollar=50000)
        self.price_per_rial = PricePerRial.objects.create(currency='USD', per_rial=42000)

    def test_create_buy_order_success(self):
        data = {"currency_name": "bitcoin", "num_of_cryptos": 1}
        response = self.client.post('/api/buyorder/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "Buy order processed successfully")

    def test_create_buy_order_invalid_currency(self):
        data = {"currency_name": "invalid_currency", "num_of_cryptos": 1}
        response = self.client.post('/api/buyorder/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], "Invalid currency name")

    @patch('buyorder.views.BuyOrderView.pay_with_zarinpal')
    def test_create_buy_order_payment_failed(self, mock_pay_with_zarinpal):
        mock_pay_with_zarinpal.return_value = {"success": False}
        data = {"currency_name": "bitcoin", "num_of_cryptos": 1}
        response = self.client.post('/api/buyorder/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], "Payment failed")

    @patch('buyorder.views.BuyOrderView.buy_from_exchange')
    def test_create_buy_order_buy_failed(self, mock_buy_from_exchange):
        mock_buy_from_exchange.return_value = {"success": False}
        data = {"currency_name": "bitcoin", "num_of_cryptos": 1}
        response = self.client.post('/api/buyorder/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['error'], "Buy order failed")