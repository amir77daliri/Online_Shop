from rest_framework import serializers
from .models import Order, OrderItem
from cart.cart import Cart
from Accounts.models import Address
from product.models import Color
from django.db import transaction
from decimal import Decimal


class OrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderSerializer(serializers.Serializer):
    address_id = serializers.IntegerField()
    price = serializers.DecimalField(read_only=True, max_digits=14, decimal_places=2)
    paid = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        request = self.context['request']
        cart = Cart(request)
        total_price = 0
        items = []
        for item in cart:
            items.append({
                'product': item['product'],
                'color': item['color'],
                'quantity': item['quantity']

            })
            total_price += item['total_price']
        if len(items) < 1:
            raise serializers.ValidationError("سبد خرید خالی است.")
        with transaction.atomic():
            order = Order.objects.create(
                user=request.user,
                price=Decimal(total_price),
                address=Address.objects.get(id=validated_data['address_id'])
            )

            for item in items:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    color=Color.objects.get(name=item['color']),
                    quantity=item['quantity']
                )
            cart.clear()
        return order
