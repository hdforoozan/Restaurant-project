# Generated by Django 2.1 on 2019-03-31 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_employee'),
        ('Food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='store',
            field=models.ManyToManyField(to='Store.Store'),
        ),
    ]
