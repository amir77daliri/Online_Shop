from rest_framework import serializers
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'slug', 'price', 'image', 'available')
