# Generated by Django 4.1.7 on 2023-02-23 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0004_alter_category_options_rename_name_fooditem_size_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fooditem",
            name="size",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="product.categorysize",
            ),
        ),
    ]