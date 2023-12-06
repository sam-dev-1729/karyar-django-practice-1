# Generated by Django 4.2.7 on 2023-12-06 11:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Orders",
            new_name="Order",
        ),
        migrations.RenameModel(
            old_name="Products",
            new_name="Product",
        ),
        migrations.RenameModel(
            old_name="Sellers",
            new_name="Seller",
        ),
        migrations.AlterModelOptions(
            name="order",
            options={"verbose_name_plural": "Orders"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name_plural": "Products"},
        ),
        migrations.AlterModelOptions(
            name="seller",
            options={"verbose_name_plural": "Sellers"},
        ),
        migrations.RenameField(
            model_name="product",
            old_name="seller",
            new_name="sellman",
        ),
    ]
