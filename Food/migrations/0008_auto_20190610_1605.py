# Generated by Django 2.1 on 2019-06-10 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0007_auto_20190403_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='food',
            name='pub_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
