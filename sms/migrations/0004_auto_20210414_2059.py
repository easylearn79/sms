# Generated by Django 3.1.1 on 2021-04-14 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_auto_20210414_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]