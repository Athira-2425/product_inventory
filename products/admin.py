from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'category', 'price', 'stock','added_date')
    search_fields = ('name', 'sku')
    list_filter = ('category',)
