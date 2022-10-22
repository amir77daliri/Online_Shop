from django.db import models
from django.utils.text import slugify


class Color(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='نام کالا')
    slug = models.SlugField(max_length=200, blank=True)
    description = models.TextField(blank=True, null=True,verbose_name='توضیحات')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='قیمت')
    color = models.ManyToManyField(Color)
    available = models.BooleanField(default=True, verbose_name='موجود میباشد؟')
    image = models.ImageField(upload_to='product/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name}')
        super(Product, self).save(*args, **kwargs)