from rest_framework import serializers
from orders.models import Order, OrderItem

class OrderSerializer(serializers.ModelSerializer):
    #add stringrelated field to show username and shippingaddress instead of id
    # shipping_address = serializers.StringRelatedField(many=True)
    class Meta:
        model = Order
        fields = ('id','user','shipping_address', 'order_time','order_status')

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id','order','product','quantity','price')