# Generated by Django 4.0.2 on 2022-03-09 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Eshopper', '0005_alter_product_condition'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
