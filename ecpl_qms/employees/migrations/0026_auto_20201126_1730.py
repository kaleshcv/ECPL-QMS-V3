# Generated by Django 3.1.3 on 2020-11-26 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0025_auto_20201126_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmonitorinform',
            name='closed_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='emailmonitoringform',
            name='closed_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='inboundmonitoringform',
            name='closed_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='outboundmonitoringform',
            name='closed_date',
            field=models.DateTimeField(null=True),
        ),
    ]
