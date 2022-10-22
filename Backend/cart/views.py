from rest_framework import generics, status, serializers
from rest_framework.response import Response
from .cart import Cart
from .serializers import AddtoCartSerializer, DeleteFromCartSerializer
from product.models import Product, Color
from product.serializers import ProductDetailSerializer


class CartDetailApi(generics.GenericAPIView):

    def get(self, request):
        cart = Cart(request)
        data = []
        for item in cart:
            product = ProductDetailSerializer(item['product']).data
            item['product'] = product
            data.append(item)
        if len(data) < 1:
            return Response({'msg': 'سبد خرید خالی است.'})
        return Response(data)


class AddToCartApi(generics.GenericAPIView):
    serializer_class = AddtoCartSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        try:
            product = Product.objects.get(id=data['product_id'])
        except Product.DoesNotExist:
            raise serializers.ValidationError("محصول مورد نظر موجود نیست")
        if not product.available:
            return Response({'msg': 'محصول مورد نظر موجود نمی باشد!'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            color = Color.objects.get(name=data['color'])
        except Color.DoesNotExist:
            raise serializers.ValidationError('چنین رنگی موجود نیست.')
        if color not in product.color.all():
            return Response({'msg': 'محصول با رنگ مورد نظر موجود نیست.'}, status=status.HTTP_400_BAD_REQUEST)

        cart = Cart(request)
        cart.add_to_cart(product, data['quantity'])
        return Response({'msg': 'محصول به سبد خرید اضافه شد.'}, status=status.HTTP_200_OK)


class DeleteFromCart(generics.GenericAPIView):
    serializer_class = DeleteFromCartSerializer

    def post(self, request):
        cart = Cart(request)
        my_ser = self.serializer_class(data=request.data)
        my_ser.is_valid(raise_exception=True)
        product_id = my_ser.validated_data.get('product_id')
        cart.remove_from_cart(product_id)
        return Response({'msg': 'محصول از سبد خرید حذف شد.'}, status=status.HTTP_200_OK)
