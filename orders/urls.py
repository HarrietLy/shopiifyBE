from django.urls import path
from .views import *

urlpatterns =[
    path('orders/',OrderListView.as_view()),
    path('orders/<int:orderId>/',OrderDetailsView.as_view()),
    path('orders/byuser/<int:userId>/',OrderbyUserListView.as_view()),
    path('orderitems/<int:orderId>/',OrderItemDetailsView.as_view()),
]