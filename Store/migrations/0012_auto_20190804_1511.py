# Generated by Django 2.2.2 on 2019-08-04 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0011_store_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='Store.Store'),
        ),
    ]
