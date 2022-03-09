from .models import Order, OrderItem
from .serializers import *
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.
class OrderListView(APIView):
    #get all orders for admin to view at FE
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    # post a new order: {user, address}
    def post(self,request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderbyUserListView(APIView):
    def get(self, request, userId):
        orders = Order.objects.filter(user_id=userId)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class OrderDetailsView(APIView):
    #get all details (user, shipping address, status) of an order
    # edit an order ( only when admin update order status)
    # can delete order ( allow user to cancel order that are pending only) if response.data.get('status')==='pending'

    def get_object(self,orderId):
        try:
            return Order.objects.get(id=orderId)
        except Order.DoesNotExist:
            raise Http404
    def get(self, request,orderId):
        order = self.get_object(orderId)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    def put(self,request, orderId):
        order = self.get_object(orderId)
        serializer = OrderSerializer(order, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serilizer.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self,request, orderId):
        order = self.get_object(orderId)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderItemDetailsView(APIView):
    # get all orderitems by orderid, 
    # post each productid to create order item of a newly created order, this post action should be done immediately after post to order, in the FE

    def get_object(self,orderId):
        try:
            return OrderItem.objects.filter(order_id=orderId)
        except OrderItem.DoesNotExist:
            raise Http404

    def get(self,request, orderId):
        orderitems = self.get_object(orderId)
        print("orderitems",orderitems)
        serializer = OrderItemSerializer(orderitems, many=True)
        return Response(serializer.data)

    def post(self,request,orderId):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# cannot put orderitem or delete order item 