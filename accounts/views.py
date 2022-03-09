# accounts.views.py

# Here, we are adding all of the necessary imports for our LoginView
from django.shortcuts import render, redirect
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, TokenSerializer, AddressSerializer
from django.contrib.auth.models import User
from .models import Address
from django.contrib.auth import authenticate, login

# JWT settings
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

class LoginView(generics.ListCreateAPIView):
    """
    POST user/login/
    """

    # This permission class will overide the global permission class setting
    # Permission checks are always run at the very start of the view, before any other code is allowed to proceed.
    # The permission class here is set to AllowAny, which overwrites the global class to allow anyone to have access to login.
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    #overriding parent's post methods
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        print('request',request.data)
        print('user',user)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            refresh = RefreshToken.for_user(user)
            serializer = TokenSerializer(data={
                # using DRF JWT utility functions to generate a token
                "token": str(refresh.access_token),
                "username":username
                })
        
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegisterUsersView(generics.ListCreateAPIView):
    """
    POST user/signup/
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username or not password or not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(status=status.HTTP_201_CREATED)

#get user by username, so we can call after logging in succesfully in the FE to get userID
class UserbyUsernameView(APIView):
    def get(self,request,username):
        try:
            user = User.objects.get(username=username)
        except:
            return Response({"status":'not ok'})

        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserbyUserIdView(APIView):
    def get(self,request,userId):
        try:
            user = User.objects.get(id=userId)
        except:
            return Response({"status":'not ok'})

        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserListView(APIView):
    def get(self,request):
        
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

#LogoutView
# class LogoutView(APIView):
#     permission_classes=(permissions.IsAuthenticated,)

#     def post(self,request):
#         if self.request.data.get('all'):
#             token: OutstandingToken
#             for token in OutstandingToken.objects.filter(user=request.user):
#                 _, _ = BlacklistedToken.objects.get_or_create(token=token)
#             return Response({"status": "ok, goodbye, all refresh tokens blacklisted"})
#         refresh_token = self.request.data.get('refresh_token')
#         token = RefreshToken(token=refresh_token)
#         token.blacklist()
#         return Response({"status": "ok"})

#get and post routes for each user
# class GetAddressView(APIView):
#     def get(self,request, user_id):
#         try:
#             address = Address.objects.get(user_id = user_id)
#         except:
#             return Response({"status":"not ok"})
#         serializer = AddressSerializer(address)
#         return Response(serializer.data)

        
#get  post routes for  all address
class ListAddressView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


#get, put, delete route for each address
class DetailAddressView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressByUserView(APIView):
    def get_object(self,userId):
        try:
            return Address.objects.filter(user=userId)
        except CartItem.DoesNotExist:
            raise Http404

    def get(self, request, userId):
        addresses= self.get_object(userId)
        serializer = AddressSerializer(addresses,many=True)
        print("serializer",serializer)
        return Response(serializer.data)
