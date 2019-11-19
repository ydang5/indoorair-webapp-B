from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.Serializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField(required = False)
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    password = serializers.CharField(write_only = True)


    def create(self, validated_data):
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name', None)
        email = validated_data.get('email')
        username = validated_data.get('username')
        password = validated_data.get('password')

        user = User.objects.create_user(username, email, password)
        user.last_name = last_name
        user.first_name = first_name
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        username = validated_data.get('username', None)
        password = validated_data.get('password', None)
        request=self.context.get(request)
        try:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return user
        except Exception as e:
            print(e)
        raise serializers.ValidationError('Please enter valid username and password')
