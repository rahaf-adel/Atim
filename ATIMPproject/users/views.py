from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import userRegisterSerializer


# Create your views here.

@api_view(['POST'])
def register_user(request: Request):
    """A simple function that register user to the system"""
    user_serializer = userRegisterSerializer(data=request.data)
    if user_serializer.is_valid():
        new_user = User.objects.create_user(**user_serializer.data)
        new_user.save()
        return Response({"msg": "created user successfully"})
    else:
        print(user_serializer.errors)
        return Response({"msg": "Couldn't create suer"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request: Request):
    """A simple function that login user to the system"""
    if 'username' in request.data and 'password' in request.data:
        user = authenticate(request, username=request.data['username'], password=request.data['password'])
        if user is not None:
            # create the token , then give the token to the user in the response (header in postman)
            token = AccessToken.for_user(user)
            print(login_user.__doc__)
            responseData = {
                "msg": "Wellcome to Atim system >> Your token is ready",
                "token": str(token)
            }
        else:
            responseData = {
                "msg": "There is an error logging in , Try again !..."}
        return Response(responseData)
