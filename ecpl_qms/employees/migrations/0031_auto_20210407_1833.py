# Generated by Django 3.1.7 on 2021-04-07 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0030_auto_20210407_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmonitoringformpodfather',
            name='ticket_no',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='famehousemonitoringform',
            name='ticket_no',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='flamonitoringform',
            name='order_id',
            field=models.CharField(max_length=50),
        ),
    ]