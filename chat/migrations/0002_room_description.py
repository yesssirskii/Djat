# Generated by Django 3.2.8 on 2022-08-31 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.TextField(default='0'),
        ),
    ]
