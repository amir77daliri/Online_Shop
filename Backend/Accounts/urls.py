from django.urls import path
from .views import (
    LoginApi,
    RegisterApi,
    RegisterVerifyApi
)
urlpatterns = [
    path('login/', LoginApi.as_view()),
    path('signup/', RegisterApi.as_view()),
    path('signup/verify/', RegisterVerifyApi.as_view()),
]
