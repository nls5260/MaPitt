# Generated by Django 2.1.5 on 2019-01-26 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20190126_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='isElective',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='requiredForMajor',
            field=models.BooleanField(default=False),
        ),
    ]
