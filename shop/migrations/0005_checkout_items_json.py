# Generated by Django 4.2.5 on 2023-10-03 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='items_json',
            field=models.CharField(default='', max_length=5000),
        ),
    ]