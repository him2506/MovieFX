# Generated by Django 3.0.6 on 2021-03-27 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshow',
            name='English',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tvshow',
            name='Hindi',
            field=models.BooleanField(default=False),
        ),
    ]