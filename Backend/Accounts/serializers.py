from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11, required=True)
    email = serializers.EmailField(required=False)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError("پسوردها مطابقت ندارند.")
        return attrs

    def create(self, validated_data):
        user = None
        try:
            user = User.objects.get(
                phone_number=validated_data['phone_number']
            )
        except User.DoesNotExist:
            user = User.objects.create_user(
                phone_number=validated_data['phone_number'],
                password=validated_data['password1'],
                email=validated_data.get('email') or None
            )
            user.is_active = False
            user.save()
        return user


class UserRegisterVerifySerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11, required=True)
    code = serializers.CharField(required=True)
