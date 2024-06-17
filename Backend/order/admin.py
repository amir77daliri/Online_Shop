from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'price', 'paid', 'create')
    list_filter = ('paid', 'create')
    search_fields = ('user__username', 'create')
    inlines = [OrderItemInline]  # Register the inline model
