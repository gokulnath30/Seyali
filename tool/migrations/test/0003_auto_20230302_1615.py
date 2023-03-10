# Generated by Django 3.2.16 on 2023-03-02 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0002_alter_person_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(default='NA', max_length=200)),
                ('imag_path', models.CharField(default='NA', max_length=200)),
                ('owner_name', models.CharField(default='NA', max_length=200)),
                ('members', models.CharField(default='NA', max_length=500)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
