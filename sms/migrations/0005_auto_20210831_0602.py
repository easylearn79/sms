# Generated by Django 3.1.5 on 2021-08-31 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0004_remove_student_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='term',
            new_name='semester',
        ),
    ]
