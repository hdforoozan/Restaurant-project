# Generated by Django 2.2.2 on 2019-09-02 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0003_comment_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='food',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Food.Food'),
        ),
    ]
