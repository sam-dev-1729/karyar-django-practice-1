from django.contrib import admin

from .models import Category, Customer, Order, Product, Seller


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price", "salesman"]
    list_display_links = ["id", "title"]
    list_filter = ["title", "price", "brand"]
    search_fields = ["title", "price", "brand", "category"]


class SellerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "phone"]
    list_display_links = ["id", "name"]
    list_filter = ["name", "phone"]
    search_fields = ["name"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "owner"]
    list_display_links = ["id", "owner"]
    list_filter = ["owner", "created_at"]
    search_fields = ["owner", "created_at"]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "family", "phone"]
    list_display_links = ["id", "name"]
    list_filter = ["id", "name", "phone"]
    search_fields = ["name", "phone"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Customer, CustomerAdmin)
