# Generated by Django 3.1.6 on 2021-02-11 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cityapp', '0003_bus_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='display',
            name='timeinterval',
            field=models.CharField(default='8:00', max_length=25),
        ),
    ]