from .models import CartItem, Product
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class CartItemCreateView(APIView):

    def post(self,request):
        print('post request.data.get("product")', request.data.get("product"))
        #TODO: add validation to check if there if any request.data.get(product)
        serializer = CartItemSerializer(data = request.data) # request data from FE will be in the form of {"userId":  , "productId": , quantity}
        print("serializer",serializer)
        quantity = request.data.get("quantity")
        product = Product.objects.get(id=request.data.get("product"))
        if quantity > product.stock:
            print(f"The order_quantity ({quantity}) is more than total stock ({product.stock})")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
  

# view all cartitem and delete all cartitems ( upon paid)
class CartItemByUserView(APIView):
    def get_object(self,userId):
        try:
            return CartItem.objects.filter(user_id=userId)
        except CartItem.DoesNotExist:
            raise Http404

    #load all cart items for each user
    def get(self, request, userId):
        cartitem = self.get_object(userId)
        serializer = CartItemSerializer(cartitem,many=True)
        print("serializer",serializer)
        return Response(serializer.data)


    #upon payment, all cart items under user will be deleted
    def delete(self,request,userId):
        cartitem = self.get_object(userId)
        cartitem.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


# use this route to check if an productid is already in the cart, if yes, send put, if not, send post
class CartItemByUserByProductView(APIView):
    def get_object(self,userId,productId):
        try:
            return CartItem.objects.filter(user_id=userId).filter(product_id=productId)#ok to assume there is only one instance for each useridxproductid pair
        except CartItem.DoesNotExist:
            raise Http404

    def get(self, request, userId,productId):
        cartitem = self.get_object(userId,productId)
        serializer = CartItemSerializer(cartitem, many=True)
        print("serializer",serializer)
        return Response(serializer.data)

    #put
    def put(self, request, userId,productId):
        cartitem = self.get_object(userId, productId)[0]
        serializer = CartItemSerializer(cartitem,data=request.data)
        print("serializer",serializer)
        if serializer.is_valid():
            print('serializer is valid')
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete
    def delete(self,request, userId, productId):
        cartitem = self.get_object(userId,productId)
        cartitem.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)



