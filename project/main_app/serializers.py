from rest_framework import serializers
from django.core.validators import EmailValidator
from .models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[EmailValidator()], required=True)
    class Meta:
        model = User
        fields = ['name', 'email', 'age']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_email(self, value):

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate_age(self, value):
        if not (0 <= value <= 120):
            raise serializers.ValidationError("Age must be between 0 and 120.")
        return value