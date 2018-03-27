# Generated by Django 2.0.3 on 2018-03-27 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.DateTimeField(auto_created=True)),
                ('song_count', models.IntegerField()),
                ('description', models.TextField(null=True)),
                ('album_cover', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True)),
                ('description', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteSong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_date', models.DateTimeField(auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=150)),
                ('surname', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time', models.DateTimeField()),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Singer')),
            ],
        ),
        migrations.CreateModel(
            name='SongType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.SongType'),
        ),
        migrations.AddField(
            model_name='singer',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.SongType'),
        ),
        migrations.AddField(
            model_name='favoritesong',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Song'),
        ),
        migrations.AddField(
            model_name='favoritesong',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.User'),
        ),
        migrations.AddField(
            model_name='album',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.Comment'),
        ),
        migrations.AddField(
            model_name='album',
            name='singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Singer'),
        ),
        migrations.AddField(
            model_name='album',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.SongType'),
        ),
    ]
