# Generated by Django 4.1.7 on 2023-02-23 07:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FoodImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="static/")),
                (
                    "description",
                    models.TextField(blank=True, max_length=250, null=True),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[("Solid", "Solid"), ("Grain", "Grain")], max_length=10
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FoodItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("market_name", models.CharField(max_length=250)),
                ("location", models.CharField(max_length=500)),
                ("size", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="product.foodimage",
                    ),
                ),
            ],
        ),
    ]
