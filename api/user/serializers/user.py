from django.contrib.auth.models import update_last_login
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['role'] = self.user.role
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return data

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def create(self, validated_data):
        return super().create(validated_data)


class UserModelSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=8, write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'role',
            'address',
            'birthday',
            'started_at',
            'order_number',
            'note',
            'salary',
            'password',
            'password2'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password2(self, password2):
        password = self.context['request'].data.get('password')
        if password != password2:
            raise serializers.ValidationError('Passwords are not the same')
        return password2

    def create(self, validated_data):
        password2 = validated_data.pop('password2')
        user = super().create(validated_data)
        user.set_password(password2)
        user.save(update_fields=('password',))
        return user
