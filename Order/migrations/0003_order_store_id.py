# Generated by Django 2.2.2 on 2019-08-31 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_auto_20190831_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='store_id',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
