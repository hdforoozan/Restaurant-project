# Generated by Django 2.2.2 on 2019-08-25 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0018_auto_20190825_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='run_out',
            field=models.BooleanField(default=False),
        ),
    ]