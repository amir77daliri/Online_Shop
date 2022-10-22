from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Brand
from rest_framework.pagination import PageNumberPagination
from .serializers import (
    ProductListSerializer,
    BrandListSerializer,
    ProductDetailSerializer,
)


class BrandListApi(generics.ListAPIView):
    serializer_class = BrandListSerializer

    def get_queryset(self, category_slug):
        queryset = Brand.objects.filter(category__slug=category_slug)
        return queryset

    def get(self, request, category_slug):
        queryset = self.get_queryset(category_slug)
        data = self.serializer_class(queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class ProductPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 4


class ProductListApi(generics.ListAPIView):
    serializer_class = ProductListSerializer
    pagination_class = ProductPagination
    filterset_fields = ['category', 'available', 'brand_name__name']
    def get_queryset(self):
        return Product.objects.all().order_by('-created_at')


class ProductDetailApi(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer

    def get(self, request, pk, slug):
        try:
            product = Product.objects.get(pk=pk, slug=slug)
        except Product.DoesNotExist:
            return Response({'msg': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        related_products = Product.objects.filter(brand_name=product.brand_name).exclude(pk=pk)[:20]
        product = self.serializer_class(product).data
        serialize_related_products = ProductListSerializer(related_products, many=True).data
        content = {
            'product': product,
            'related_products': serialize_related_products
        }
        return Response(content, status=status.HTTP_200_OK)


