# Generated by Django 2.1 on 2019-06-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0010_remove_food_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
