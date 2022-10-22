from django.urls import path
from .views import (
    ProductListApi,
    BrandListApi,
    ProductDetailApi
)
urlpatterns = [
    path('', ProductListApi.as_view(), name='products-list'),
    path('brands/<slug:category_slug>', BrandListApi.as_view()),
    path('<int:pk>/<slug:slug>', ProductDetailApi.as_view()),

]
