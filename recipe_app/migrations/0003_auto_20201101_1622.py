# Generated by Django 3.1.2 on 2020-11-01 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0002_auto_20201101_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=30, verbose_name='title'),
        ),
    ]
