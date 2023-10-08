# Generated by Django 4.2.5 on 2023-10-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckOut',
            fields=[
                ('check_out_id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=30)),
                ('province', models.CharField(default='', max_length=30)),
                ('zip', models.CharField(default='', max_length=30)),
            ],
        ),
    ]