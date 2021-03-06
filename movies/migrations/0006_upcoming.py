# Generated by Django 3.0.6 on 2021-03-22 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20210322_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpComing',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_name', models.CharField(max_length=200)),
                ('year', models.CharField(default='', max_length=50)),
                ('image', models.ImageField(default='', upload_to='img')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
