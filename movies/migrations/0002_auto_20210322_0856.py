# Generated by Django 3.0.6 on 2021-03-22 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='category',
        ),
        migrations.AddField(
            model_name='movie',
            name='action',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='adventure',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='animation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='comedy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='crime',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='documentry',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='drama',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='family',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='fantasy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='history',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='horror',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='musical',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='mystery',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='sci_fi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='sport',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='thriller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='tvshow',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='war',
            field=models.BooleanField(default=False),
        ),
    ]
