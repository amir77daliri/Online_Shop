from rest_framework import serializers


class AddtoCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1, max_value=9)
    color = serializers.CharField(max_length=20)


class DeleteFromCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()


class AddtoCartResponseSerializer(serializers.Serializer):
    msg = serializers.CharField(max_length=200)
