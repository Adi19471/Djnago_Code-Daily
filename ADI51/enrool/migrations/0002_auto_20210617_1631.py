# Generated by Django 3.0 on 2021-06-17 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]