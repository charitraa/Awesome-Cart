# Generated by Django 4.2.5 on 2023-10-08 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_orderupdate_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderupdate',
            name='order_id',
        ),
    ]