from django.db import models

# Create your models here.

class SongType(models.Model):
    name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name
class Singer(models.Model):
    name = models.TextField(max_length=150,null=False)
    surname = models.TextField(max_length=150,null=False)
    type = models.ForeignKey(SongType,null=True,on_delete=models.SET_NULL)

class Song(models.Model):
    name = models.CharField(max_length=100,null=False)
    type = models.ForeignKey(SongType,null=True, on_delete=models.SET_NULL)
    time = models.DateTimeField(null=False)
    singer = models.ForeignKey(to=Singer,on_delete=models.CASCADE)

class User(models.Model):
    user_name = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=150,null=False)
    password = models.CharField(max_length=150, null=False)

class Album(models.Model):
    type = models.ForeignKey(SongType,null=True,on_delete=models.SET_NULL)
    song_count = models.IntegerField(null=False)
    description = models.TextField(null=True)
    album_cover = models.TextField(null=True)
    release_date = models.DateTimeField(auto_created=True)
    singer = models.ForeignKey(Singer,on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    album = models.ForeignKey(to=Album,on_delete=models.CASCADE)
    description = models.TextField(max_length=255,null=False)
    created_date = models.DateTimeField(auto_created=True)

class FavoriteSong(models.Model):
    favorite_date = models.DateTimeField(auto_created=True)
    song = models.ForeignKey(Song,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)