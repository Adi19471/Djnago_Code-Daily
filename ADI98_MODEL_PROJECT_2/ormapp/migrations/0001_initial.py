# Generated by Django 3.0 on 2021-09-19 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('scale_tpe', models.CharField(max_length=220)),
                ('scale_price', models.IntegerField()),
            ],
        ),
    ]