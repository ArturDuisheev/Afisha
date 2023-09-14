from rest_framework import serializers
from account import models as a_m


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = a_m.User
        fields = ('id', 'email', 'first_name', 'last_name','confirmation_code', 'password')

    def create(self, validated_data):
        user = a_m.User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = a_m.User
        fields = ('id', 'email', 'password')


class UserConfirmationSerializer(serializers.Serializer):
    confirmation_code = serializers.CharField()
    

