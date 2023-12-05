from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Category(models.Model):
    name: models.CharField = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Products(models.Model):
    name: models.CharField = models.CharField(max_length=150)
    brand: models.CharField = models.CharField(max_length=150)
    price: models.PositiveBigIntegerField = models.PositiveBigIntegerField()
    created_at: models.DateTimeField = models.DateTimeField(auto_now=True)
    updated_at: models.DateTimeField = models.DateTimeField(
        blank=True, null=True
    )
    category: models.ManyToManyField = models.ManyToManyField(Category)
    seller: models.ForeignKey = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    # seller: models.ForeignKey = models.ForeignKey(
    #     Seller, on_delete=models.CASCADE
    # )
    def __str__(self) -> str:
        return self.name


class Sellers(models.Model):
    name: models.CharField = models.CharField(max_length=150)
    address: models.TextField = models.TextField()
    phone: models.CharField = models.CharField(max_length=11)
    banck_account: models.CharField = models.CharField(max_length=100)
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    # products = models.ManyToManyField(Products)

    def __str__(self) -> str:
        return self.name


class Orders(models.Model):
    owner: models.ForeignKey = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    products: models.ForeignKey = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
    )
    quantity: models.IntegerField = models.IntegerField()
    price: models.PositiveBigIntegerField = models.PositiveBigIntegerField()
    description: models.TextField = models.TextField()
    date: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Order"
