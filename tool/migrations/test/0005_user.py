# Generated by Django 4.0.6 on 2023-03-03 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0004_project_classes'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Project_id', models.CharField(default='NA', max_length=200)),
                ('user', models.CharField(default='NA', max_length=200)),
                ('imgCount', models.CharField(default='NA', max_length=200)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
