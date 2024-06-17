from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product, Color
from Accounts.models import Address

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    paid = models.BooleanField(default=False)
    address = models.ForeignKey(Address, related_name='ads_orders', on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = 'پرداخت شده' if self.paid else 'در انتظار پرداخت'
        return f"سفارش کاربر {self.user.get_fullname()} - {status}"

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'آیتم'
        verbose_name_plural = 'آیتم ها'