from rest_framework import serializers
from .models import Currency, Transaction, Category

class CurrencyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id','code','name')

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class WriteTransactionModelSerializer(serializers.ModelSerializer):
    currency = serializers.SlugRelatedField(slug_field='code', queryset=Currency.objects.all())
    class Meta:
        model = Transaction
        fields = ("amount", 'currency', 'date', 'description', 'category')
class ReadTransactionModelSerializer(serializers.ModelSerializer):
    currency = CurrencyModelSerializer()
    category = CategoryModelSerializer()
    class Meta:
        model = Transaction
        fields = ('id',"amount", 'currency', 'date', 'description', 'category')
        read_only_fields = fields