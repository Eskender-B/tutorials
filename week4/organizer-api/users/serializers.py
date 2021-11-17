from rest_framework import serializers
from .models import User
from .validators import validate_password_strength


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        label="Email address",
    )
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        label="Password",
        validators=[validate_password_strength],
    )
    password2 = serializers.CharField(
        write_only=True,
        min_length=8,
        label="Confirm password",
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password", "password2", "avatar")

    def validate(self, attrs):
        password2 = attrs.pop("password2")
        if password2 != attrs.get("password"):
            msg = "Your passwords do not match."
            raise serializers.ValidationError({"password2": msg})
        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = self.Meta.model.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "date_joined", "avatar")
        read_only_fields = ("email", "date_joined")

    
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'email', 'date_joined')

        extra_kwargs = {
            "url": {
                "lookup_field": "pk",
                "view_name": "users:user-detail",
            }
        }
