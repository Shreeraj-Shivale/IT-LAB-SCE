# Generated by Django 2.0.1 on 2018-04-22 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_remove_accountstatus_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountstatus',
            name='user_name',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
