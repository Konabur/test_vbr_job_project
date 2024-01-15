from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    def validate_email(self, value):
        """
        Валидация email.
        """
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email уже используется.")
        return value

    def validate_password(self, value):
        """
        Валидация пароля.
        """
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return value