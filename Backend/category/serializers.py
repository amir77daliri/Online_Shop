from rest_framework import serializers
from .models import Category


class CategoryListSerializer(serializers.ModelSerializer):
    def get_sub(self, obj):
        if obj.is_sub:
            return "%s" % obj.sub_category

    sub_category = serializers.SerializerMethodField('get_sub')

    class Meta:
        model = Category
        fields = "__all__"



