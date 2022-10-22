from django.urls import path
from .views import (
    ProductListApi,
)
urlpatterns = [
    path('', ProductListApi.as_view(), name='products-list'),
]
