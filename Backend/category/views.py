from django.db.models import Prefetch
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from rest_framework import status
from rest_framework.response import Response


class CategoryListApi(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.filter(parent_category__isnull=True).prefetch_related('children').order_by('id')
        return queryset

    def get(self, request):
        queryset = self.get_queryset()
        data = self.serializer_class(queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK)



