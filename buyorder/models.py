from django.db import models

class Crypto(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)

class Price(models.Model):
    crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE)
    price_per_dollar = models.DecimalField(max_digits=10, decimal_places=2)

class PricePerRial(models.Model):
    currency = models.CharField(max_length=10)
    per_rial = models.DecimalField(max_digits=10, decimal_places=2)