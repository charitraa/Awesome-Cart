# Generated by Django 4.2.5 on 2023-10-04 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_alter_orderupdate_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='order_id',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
