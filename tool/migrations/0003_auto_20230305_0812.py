# Generated by Django 3.2.16 on 2023-03-05 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0002_members_imag_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='imag_path',
            field=models.CharField(default='NA', max_length=10000),
        ),
        migrations.AlterField(
            model_name='project',
            name='imag_path',
            field=models.CharField(default='NA', max_length=10000),
        ),
    ]