from rest_framework import generics
from .models import Category
from .serializers import CategoryListSerializer
from rest_framework import status
from rest_framework.response import Response


class CategoryListApi(generics.ListAPIView):
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset

    def get(self, request):
        queryset = self.get_queryset()
        data = self.serializer_class(queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK)



