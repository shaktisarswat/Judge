# Generated by Django 4.0.6 on 2022-07-19 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_userdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserDetails',
            new_name='UserDetail',
        ),
    ]
