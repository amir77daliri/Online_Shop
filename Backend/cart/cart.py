from product.models import Product
CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}

        self.cart = cart

    def add_to_cart(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }
        self.cart[product_id]['quantity'] += quantity
        if self.cart[product_id]['quantity'] < 10:
            self.save()
        else:
            self.cart[product_id]['quantity'] = 9
            self.save()

    def remove_from_cart(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart.keys():
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['total_price'] = float(item['price']) * item['quantity']
            yield item

    def save(self):
        self.session.modified = True
