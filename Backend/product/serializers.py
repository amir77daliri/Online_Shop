from rest_framework import serializers
from .models import Product, Brand, Color
from category.serializers import CategoryListSerializer


class BrandListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('name', )


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'slug', 'price', 'image', 'available')


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ('name', )


class ProductDetailSerializer(serializers.ModelSerializer):
    color = ColorSerializer(read_only=True, many=True)
    brand_name = BrandListSerializer(read_only=True)
    category = CategoryListSerializer(read_only=True)

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at')