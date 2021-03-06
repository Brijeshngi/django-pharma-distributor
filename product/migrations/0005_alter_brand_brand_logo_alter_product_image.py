# Generated by Django 4.0.1 on 2022-03-06 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_logo',
            field=models.ImageField(upload_to='brand_logo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product_image'),
        ),
    ]
