# Generated by Django 2.2.1 on 2019-08-18 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_ccat_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='CDAC2019Aug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=111, unique=True)),
                ('status', models.CharField(default='New', max_length=111)),
                ('view', models.CharField(default='No', max_length=111)),
            ],
        ),
    ]
