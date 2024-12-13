from rest_framework import serializers

class BuyOrderSerializer(serializers.Serializer):
    currency_name = serializers.CharField(max_length=100)
    num_of_cryptos = serializers.IntegerField()