# Generated by Django 2.2.1 on 2019-10-23 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineTest', '0006_auto_20191023_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='a',
        ),
        migrations.RemoveField(
            model_name='score',
            name='ans',
        ),
        migrations.RemoveField(
            model_name='score',
            name='b',
        ),
        migrations.RemoveField(
            model_name='score',
            name='c',
        ),
        migrations.RemoveField(
            model_name='score',
            name='d',
        ),
        migrations.RemoveField(
            model_name='score',
            name='qtype',
        ),
        migrations.AddField(
            model_name='score',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
