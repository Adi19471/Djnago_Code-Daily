# Generated by Django 3.0 on 2021-06-07 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_student_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='comment',
        ),
    ]
