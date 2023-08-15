from django.contrib import admin

from .models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "price"]
    list_filter = ["category"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["id", "name"]
