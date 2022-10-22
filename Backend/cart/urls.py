from django.urls import path
from .views import (
    AddToCartApi,
    CartDetailApi,
    DeleteFromCart
)
urlpatterns = [
    path('details', CartDetailApi.as_view()),
    path('add/', AddToCartApi.as_view()),
    path('delete-item/', DeleteFromCart.as_view()),
]
