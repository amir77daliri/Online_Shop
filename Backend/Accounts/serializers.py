from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Address


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


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        exclude = ('user', )

    def create(self, validated_data):
        validated_data['user'] = self.context['user']
        print(validated_data)
        address = Address.objects.create(city=validated_data['city'], state=validated_data['state'], user=validated_data['user'])
        return address

    def update(self, instance, validated_data):
        validated_data['user'] = self.context['user']
        instance.city = validated_data['city']
        instance.state = validated_data.state
        instance.save()
        return instance

