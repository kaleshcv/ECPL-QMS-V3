# Generated by Django 3.1.7 on 2021-04-02 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0026_auto_20210403_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(unique=True)),
                ('empname', models.CharField(max_length=50)),
                ('empid', models.IntegerField()),
                ('empdesi', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('teamlead', models.CharField(max_length=50)),
                ('manager', models.CharField(max_length=50)),
                ('user_id', models.IntegerField()),
                ('am', models.CharField(max_length=50)),
                ('process', models.CharField(max_length=50)),
            ],
        ),
    ]