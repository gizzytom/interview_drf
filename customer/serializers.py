from cgitb import lookup
from dataclasses import field, fields
from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class AccountBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['cardNumber','balance']

# These two are just helping serializers for swagger UI.
class AccountBalanceResponsetSerializer(serializers.Serializer):
    cardNumber = serializers.CharField(max_length=20)
    pin = serializers.CharField(max_length=6)
    amount = serializers.CharField(max_length=20)

class AccountBalanceResponseSerializer(serializers.Serializer):
    cardNumber = serializers.CharField(max_length=20)
    pin = serializers.CharField(max_length=6)
 