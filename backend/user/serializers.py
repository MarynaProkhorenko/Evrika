from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.utils.translation import gettext as _

from user.models import User
from user.email_user_welcome import get_message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "first_name", "last_name", "password", "is_staff")
        read_only_fields = ("is_staff",)
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data) -> User:
        user = get_user_model().objects.create_user(**validated_data)
        full_name = validated_data["first_name"] + " " + validated_data["last_name"]
        receiver_email = validated_data["email"]
        user_password = validated_data["password"]
        get_message(full_name, receiver_email, user_password)

        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password", ),
        style={"input_type": "password"},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(request=self.context.get("request"),
                                email=email, password=password)
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = _("Must include email and password.")
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs
