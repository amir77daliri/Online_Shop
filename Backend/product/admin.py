from django.contrib import admin
from .models import Product, Color, Brand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'colors', 'available']

    def colors(self, obj):
        return obj.color.first()


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
