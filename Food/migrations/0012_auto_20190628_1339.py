# Generated by Django 2.1 on 2019-06-28 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0011_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(blank=True, height_field=200, null=True, upload_to='images/', width_field=200),
        ),
    ]
