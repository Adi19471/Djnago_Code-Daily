# Generated by Django 3.0 on 2021-06-24 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0002_auto_20210624_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]
