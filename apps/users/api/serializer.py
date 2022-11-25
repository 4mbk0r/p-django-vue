from pyexpat import model
from apps.users.models import User
from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        """ Creates and returns a new user """

        # Validating Data
        user = User(
            username=validated_data['username'],
            name=validated_data['name'],
            email=validated_data['email'],
            bith_date=validated_data['bith_date'],

        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'gender')


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'gender', 'respuesta',)


class RegistrationSerializer(serializers.ModelSerializer[User]):
    """Serializers registration requests and creates a new user."""

    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password',
            'preguntas',
        ]

    def validate_email(self, value: str) -> str:
        """Normalize and validate email address."""
        valid, error_text = email_is_valid(value)
        if not valid:
            raise serializers.ValidationError(error_text)
        try:
            email_name, domain_part = value.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            value = '@'.join([email_name, domain_part.lower()])

        return value

    def create(self, validated_data):  # type: ignore
        """Return user after creation."""
        user = User.objects.create_user(
            username=validated_data['username'], email=validated_data['email'], password=validated_data['password']
        )
        """user.bio = validated_data.get('bio', '')
        user.full_name = validated_data.get('full_name', '')
        user.save(update_fields=['bio', 'full_name'])"""
        return user
