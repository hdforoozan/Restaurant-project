# Generated by Django 2.2.2 on 2019-09-06 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0020_auto_20190905_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='foods',
            field=models.ManyToManyField(related_name='stores', to='Food.Food'),
        ),
    ]