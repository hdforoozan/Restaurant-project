# Generated by Django 2.1 on 2019-04-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0008_auto_20190403_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]