from django.db import models
from category.models import Category


class Color(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام برند')
    category = models.ManyToManyField(Category, related_name='brands')

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='نام کالا')
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True, null=True,verbose_name='توضیحات')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='قیمت')
    color = models.ManyToManyField(Color)
    available = models.BooleanField(default=True, verbose_name='موجود میباشد؟')
    image = models.ImageField(upload_to='product/images/')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True)
    brand_name = models.ForeignKey(Brand, related_name='brand_products', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name
