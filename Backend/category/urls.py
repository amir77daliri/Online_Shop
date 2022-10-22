from django.urls import path
from .views import CategoryListApi

urlpatterns = [
    path("list/", CategoryListApi.as_view()),
]
