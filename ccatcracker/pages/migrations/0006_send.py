# Generated by Django 2.2.1 on 2019-08-13 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_notify'),
    ]

    operations = [
        migrations.CreateModel(
            name='Send',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=111)),
                ('status', models.CharField(default='New', max_length=111)),
            ],
        ),
    ]