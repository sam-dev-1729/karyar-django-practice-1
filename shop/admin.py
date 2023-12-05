from django.contrib import admin

from .models import Category, Orders, Products, Sellers


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]


class ProductsAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id", "name"]
    list_filter = ["name", "price", "brand"]
    search_fields = ["name", "price", "brand", "category"]


class SellersAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "phone"]
    list_display_links = ["id", "name"]
    list_filter = ["name", "phone"]
    search_fields = ["name"]


class OrdersAdmin(admin.ModelAdmin):
    list_display = ["id", "owner"]
    list_display_links = ["id", "owner"]
    list_filter = ["owner", "date"]
    search_fields = ["owner", "date"]


admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sellers, SellersAdmin)
admin.site.register(Orders, OrdersAdmin)
