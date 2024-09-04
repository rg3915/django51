from django.contrib import admin

from .models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'category__title', 'category__type')
    search_fields = ('title', 'category__title')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'type')
