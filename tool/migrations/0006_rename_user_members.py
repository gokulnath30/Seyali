# Generated by Django 3.2.16 on 2023-03-04 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0005_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='members',
        ),
    ]