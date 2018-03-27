from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Song)
admin.site.register(Comment)
admin.site.register(Album)
admin.site.register(FavoriteSong)
admin.site.register(SongType)
admin.site.register(Singer)