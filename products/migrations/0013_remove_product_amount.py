# Generated by Django 5.1 on 2024-09-03 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_product_description_alter_product_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='amount',
        ),
    ]
