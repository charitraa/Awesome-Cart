# Generated by Django 4.2.5 on 2023-10-04 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_remove_orderupdate_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderupdate',
            name='order_id',
            field=models.IntegerField(default=0),
        ),
    ]