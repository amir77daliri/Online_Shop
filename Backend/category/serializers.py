from rest_framework import serializers
from .models import Category


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class CategorySerializer(serializers.ModelSerializer):
    children = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'children']
