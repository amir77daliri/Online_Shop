from django.urls import path
from .views import OrderListApi, OrderCreateApi


urlpatterns = [
    path('list/', OrderListApi.as_view()),
    path('submit/', OrderCreateApi.as_view())
]
