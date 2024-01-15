from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import User, Organization, Event


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'phone_number', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    @staticmethod
    def validate_email(value):
        """
        Валидация email.
        """
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email уже используется.")
        return value

    @staticmethod
    def validate_password(value):
        """
        Валидация пароля.
        """
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return value


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'title', 'description', 'address', 'postcode']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'organizations', 'image', 'date']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['preview_image'] = instance.image.url if instance.image else None
        return rep