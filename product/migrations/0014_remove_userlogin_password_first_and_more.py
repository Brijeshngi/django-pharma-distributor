# Generated by Django 4.0.1 on 2022-03-14 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_rename_firstname_userlogin_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlogin',
            name='Password_First',
        ),
        migrations.RemoveField(
            model_name='userlogin',
            name='Password_Second',
        ),
    ]