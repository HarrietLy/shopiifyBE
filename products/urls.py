from django.urls import path
# from .views import ListCategoryView, DetailCategoryView, ListProductView, DetailProductView
from .views import *

urlpatterns =[
    path('categories/',ListCategoryView.as_view()),
    path('categories/<int:pk>/', DetailCategoryView.as_view()),
    path('products/', ListProductView.as_view()),
    path('products/<int:pk>/', DetailProductView.as_view()),
]