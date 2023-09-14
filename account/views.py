import random
import string

from django.core.mail import send_mail
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import login, logout, authenticate
from rest_framework_jwt.settings import api_settings

from account import models as a_m
from account import serializers as a_s
from account import utils as a_u


class UserRegistrationView(APIView):
    serializer_class = a_s.UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        # Генерируем рандомный код
        confirmation_code = ''.join(random.choice(string.digits) for _ in range(6))

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.confirmation_code = confirmation_code
            user.is_verified = False
            user.save()

            # Отправляем код на email пользователя
            send_mail(
                'Подтверждение аккаунта',
                f'Код подтверждения: {confirmation_code}',
                'myworkingartur@gmail.com',  # Замените на вашу электронную почту
                [user.email],
                fail_silently=False,
            )

            # Возвращаем успешный ответ
            return Response({'detail': 'User registered successfully. Check your email for confirmation code.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = a_m.User.objects.filter(email=email).first()

        if user and user.check_password(password):
            if not user.is_verified:
                return Response({'detail': 'User is not activated yet.'}, status=status.HTTP_400_BAD_REQUEST)

            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)

            return Response({'token': token}, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserConfirmationView(APIView):
    serializer_class = a_s.UserConfirmationSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})

        if serializer.is_valid():
            confirmation_code = serializer.validated_data['confirmation_code']
            user = a_m.User.objects.filter(confirmation_code=confirmation_code, is_active=False).first()

            if user:
                user.is_active = True
                user.confirmation_code = None
                user.save()
                return Response({'detail': 'User has been activated.'}, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid confirmation code or user is already activated.'},
                        status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return Response({'message': 'logout is apply'}, status=status.HTTP_200_OK)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = a_s.UserSerializer(request.user)
        return Response(serializer.data)
