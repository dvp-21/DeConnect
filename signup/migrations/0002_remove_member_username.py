# Generated by Django 5.1.3 on 2024-11-07 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='username',
        ),
    ]
