# Generated by Django 2.0.1 on 2018-04-22 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicdetails',
            name='annual_income',
            field=models.IntegerField(default=0),
        ),
    ]
