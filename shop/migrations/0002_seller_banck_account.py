# Generated by Django 4.2.7 on 2023-12-07 09:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="seller",
            name="banck_account",
            field=models.CharField(default="", max_length=100),
        ),
    ]
