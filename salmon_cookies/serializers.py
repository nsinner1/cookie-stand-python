from rest_framework import serializers
from .models import Sales


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('location', 'min_customer', 'max_customer', 'avg_sales', 'manager')
        model = Sales