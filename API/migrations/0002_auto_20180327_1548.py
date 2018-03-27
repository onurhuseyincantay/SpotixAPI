# Generated by Django 2.0.3 on 2018-03-27 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='album',
            name='singer',
        ),
        migrations.RemoveField(
            model_name='album',
            name='type',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='favoritesong',
            name='song',
        ),
        migrations.RemoveField(
            model_name='favoritesong',
            name='user',
        ),
        migrations.RemoveField(
            model_name='singer',
            name='type',
        ),
        migrations.RemoveField(
            model_name='song',
            name='singer',
        ),
        migrations.RemoveField(
            model_name='song',
            name='type',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='FavoriteSong',
        ),
        migrations.DeleteModel(
            name='Singer',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
        migrations.DeleteModel(
            name='SongType',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
