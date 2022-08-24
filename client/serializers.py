from dataclasses import fields
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ('username', 'password','email','last_name','first_name','photo')
        extra_kwargs = {
            'username': {'required': True},
            'password': {'required': True},
            'email': {'required': True},
            'last_name': {'required': False},
            'first_name': {'required': False},
            'photo': {'required': False}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email = validated_data['email'],
            last_name = validated_data['last_name'],
            photo = validated_data['photo'],
            username = validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields=['id','username','photo']

