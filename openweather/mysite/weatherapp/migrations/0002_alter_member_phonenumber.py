# Generated by Django 5.1.4 on 2024-12-19 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phoneNumber',
            field=models.IntegerField(max_length=15),
        ),
    ]