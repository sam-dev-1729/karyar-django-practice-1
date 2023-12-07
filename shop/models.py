from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Person(models.Model):
    name = models.CharField(max_length=150)
    family = models.CharField(max_length=150)
    phone = models.CharField(max_length=11)
    eamil = models.EmailField()
    address = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " : " + self.name + " " + self.family


class Category(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Seller(Person):
    banck_account = models.CharField(max_length=100, default="")

    class Meta:
        verbose_name_plural = "Sellers"


class Product(models.Model):
    title = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    # Images = models.ImageField(blank=True,null=True)
    stock = models.PositiveIntegerField(default=0)
    price = models.PositiveBigIntegerField()
    category = models.ManyToManyField(Category)
    salesman = models.ForeignKey(Seller, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Products"


class Customer(Person):
    class Meta:
        verbose_name_plural = "Customers"


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Processing", "Processing"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]
    owner = models.OneToOneField(Customer, on_delete=models.CASCADE)
    order_status = models.CharField(
        max_length=15, choices=ORDER_STATUS_CHOICES, default="Pending"
    )
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cost = models.PositiveBigIntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Orders"
