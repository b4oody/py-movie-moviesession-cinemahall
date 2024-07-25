# Generated by Django 4.0.2 on 2024-07-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_cinemahall_movie_moviesession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='db.Actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='db.Genre'),
        ),
    ]
