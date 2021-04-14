# Generated by Django 2.0.1 on 2018-04-22 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_presentlocation_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('user_name', models.CharField(default=None, max_length=150)),
            ],
        ),
    ]
