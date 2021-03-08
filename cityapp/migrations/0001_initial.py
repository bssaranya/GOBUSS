# Generated by Django 3.1.6 on 2021-02-10 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityname', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Stations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stationname', models.CharField(max_length=40)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cityapp.city')),
            ],
        ),
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=125)),
                ('time', models.CharField(max_length=25)),
                ('cities', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cityapp.city')),
                ('stations', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cityapp.stations')),
            ],
        ),
    ]