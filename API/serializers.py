from rest_framework import serializers
from .models import *


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongType
        fields = ('name',)


class SingerSerializer(serializers.ModelSerializer):
    type = TypeSerializer(many=False,read_only=True)
    class Meta:
        model = Singer
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    singer = SingerSerializer(many=False,read_only=True)
    type = TypeSerializer(many=False,read_only=True)
    class Meta :
        model = Album
        fields = '__all__'