from django.contrib import admin

from .models import Category, Order, Product, Seller


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "salesman"]
    list_display_links = ["id", "name"]
    list_filter = ["name", "price", "brand"]
    search_fields = ["name", "price", "brand", "category"]


class SellerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "phone"]
    list_display_links = ["id", "name"]
    list_filter = ["name", "phone"]
    search_fields = ["name"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "owner"]
    list_display_links = ["id", "owner"]
    list_filter = ["owner", "date"]
    search_fields = ["owner", "date"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Order, OrderAdmin)
