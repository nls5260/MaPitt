# Generated by Django 2.1.5 on 2019-01-26 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='courseName',
            field=models.CharField(default='None', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.CharField(default='CS', max_length=10),
            preserve_default=False,
        ),
    ]
