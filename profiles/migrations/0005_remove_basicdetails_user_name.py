# Generated by Django 2.0.1 on 2018-04-22 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_basicdetails_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicdetails',
            name='user_name',
        ),
    ]
