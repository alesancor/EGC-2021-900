# Generated by Django 2.0 on 2021-01-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0018_auto_20210101_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='points',
        ),
        migrations.AddField(
            model_name='voting',
            name='points',
            field=models.PositiveIntegerField(default='1'),
        ),
    ]
