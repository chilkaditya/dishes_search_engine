# Generated by Django 5.0.6 on 2024-06-26 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='lat_long',
        ),
    ]