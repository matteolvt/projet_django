# Generated by Django 5.1.4 on 2025-01-09 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Prodcuts'},
        ),
    ]
