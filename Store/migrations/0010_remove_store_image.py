# Generated by Django 2.1 on 2019-06-28 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0009_store_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='image',
        ),
    ]