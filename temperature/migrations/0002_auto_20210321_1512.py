# Generated by Django 3.1.7 on 2021-03-21 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperature', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempentry',
            name='temp',
            field=models.FloatField(),
        ),
    ]
