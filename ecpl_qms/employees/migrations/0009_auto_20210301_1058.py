# Generated by Django 3.1.7 on 2021-03-01 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_auto_20210301_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='famehousemonitoringform',
            name='sh_4',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='famehousemonitoringform',
            name='sh_5',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
