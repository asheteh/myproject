# Generated by Django 2.2.1 on 2019-10-18 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_remove_center_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='city',
            field=models.CharField(default='S', max_length=100),
        ),
    ]
