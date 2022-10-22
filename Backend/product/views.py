from rest_framework import generics
from .models import Product
from rest_framework.pagination import PageNumberPagination
from .serializers import ProductListSerializer


class ProductPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 4


class ProductListApi(generics.ListAPIView):
    serializer_class = ProductListSerializer
    pagination_class = ProductPagination

    def get_queryset(self):
        return Product.objects.all()



