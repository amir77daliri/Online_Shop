from rest_framework import generics, serializers, status, permissions
from rest_framework.response import Response
from .models import Order, OrderItem


class OrderListApi(generics.ListAPIView):
    pass