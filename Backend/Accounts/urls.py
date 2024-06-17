from django.urls import path
from .views import (
    LoginApi,
    RegisterApi,
    RegisterVerifyApi,
    AddressListApi,
    AddressCreateApi
)
urlpatterns = [
    path('login/', LoginApi.as_view()),
    path('signup/', RegisterApi.as_view()),
    path('signup/verify/', RegisterVerifyApi.as_view()),
    path('get-address/', AddressListApi.as_view()),
    path('add-address/', AddressCreateApi.as_view())
]
