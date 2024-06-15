from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import (
    UserRegisterSerializer,
    UserRegisterVerifySerializer,
)
from django.contrib.auth import get_user_model
from .tasks import send_otp_code_task
from .utils import get_code_from_redis, delete_code_from_redis

User = get_user_model()


class LoginApi(ObtainAuthToken):
    pass


class RegisterApi(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user.is_active:
            content = {'msg': 'کاربری با این مشخصات از قبل موجود است!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        phone_number = serializer.validated_data['phone_number']
        send_otp_code_task.delay(phone_number)
        content = {'msg': "کد فعالسازی برای شما ارسال شد."}
        return Response(content, status=status.HTTP_201_CREATED)


class RegisterVerifyApi(generics.GenericAPIView):
    serializer_class = UserRegisterVerifySerializer
    content = [
        {'USER_NOT_FOUND': 'اطلاعات ورودی نادرست است!'},
        {'EXPIRED_CODE': 'کد منقضی شده است'},
        {'SUCCESS': 'حساب کاربری با موفقیت فعال شد.'}
    ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = User.objects.get(phone_number=serializer.validated_data['phone_number'])
        except User.DoesNotExist:
            return Response(self.content[0], status=status.HTTP_400_BAD_REQUEST)
        code = get_code_from_redis(serializer.validated_data['phone_number'])
        # print(code)
        if not code or code.decode('utf-8') != serializer.validated_data['code']:
            return Response(self.content[1], status=status.HTTP_400_BAD_REQUEST)
        user.is_active = True
        user.save()
        delete_code_from_redis(serializer.validated_data['phone_number'])
        return Response(self.content[2], status=status.HTTP_200_OK)
