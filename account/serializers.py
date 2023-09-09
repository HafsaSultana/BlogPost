from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import User


class UseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password', 'role', 'created_by','created_at']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'].lower()
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    role = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError('Invalid Login')

        try:
            validation = {
                'email': user.email,
                'password': user.password,
                'role': user.role
            }
            return validation

        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid Login")

