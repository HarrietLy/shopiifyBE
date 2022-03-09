# accounts.urls.py

from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('login/',views.LoginView.as_view(),name='auth-login'),
    path('signup/', views.RegisterUsersView.as_view(), name="user-signup"),
#     path('logout/', views.LogoutView.as_view()),
    path('users/<username>/',views.UserbyUsernameView.as_view()),
    path('users/byid/<int:userId>/',views.UserbyUserIdView.as_view()),
    path('users/',views.UserListView.as_view()),
    path('addresses/',views.ListAddressView.as_view()),
    path('addresses/<int:pk>/',views.DetailAddressView.as_view()),
    path('addresses/byuser/<int:userId>/',views.AddressByUserView.as_view()),
]