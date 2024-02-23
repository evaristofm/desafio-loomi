from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from account.models import User
from account.serializers import (
    UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer,
    UserChangePasswordSerializer
)
from account.renderes import UserRenderer
from account.auth import get_tokens_for_user


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, formart=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user=user)
            return Response({'message': 'Registration Successful', 'token': token
                             }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginview(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')

            user = authenticate(email=email, password=password)
            if user is None:
                return Response({'erros': {'non_field_errors': ['Email or Password is not valid']}},
                         status=status.HTTP_400_BAD_REQUEST)

            token = get_tokens_for_user(user)
            return Response({'message': 'Login successful', 'token': token}, status=status.HTTP_200_OK)

        return Response({'erros': {'non_field_errors': ['Email or Password is not valid']}},
                        status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDeleteView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def put(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Changed Successfully'}, status=status.HTTP_200_OK)
