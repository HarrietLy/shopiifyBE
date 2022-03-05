from django.urls import path
from .views import *

urlpatterns =[
    path('carts/',CartItemCreateView.as_view()),
    path('carts/<int:userId>/',CartItemByUserView.as_view()),
    path('carts/<int:userId>/<int:productId>/',CartItemByUserByProductView.as_view()),
]