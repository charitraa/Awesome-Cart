# Generated by Django 4.2.5 on 2023-10-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_orderupdate_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderupdate',
            old_name='timestam',
            new_name='timestamp',
        ),
        migrations.AlterField(
            model_name='orderupdate',
            name='order_id',
            field=models.IntegerField(default=''),
        ),
    ]
