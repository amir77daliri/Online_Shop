from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_sub', 'slug', 'get_subs']

    def get_subs(self, obj):
        if obj.sub_categories.all():
            a = [category.title for category in obj.sub_categories.all()]
            return " ".join(a)
