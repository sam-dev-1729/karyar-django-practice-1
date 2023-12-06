from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    price = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    category = models.ManyToManyField(Category)
    salesman = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Products"


class Seller(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField()
    phone = models.CharField(max_length=11)
    banck_account = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Sellers"


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.PositiveBigIntegerField()
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Orders"
