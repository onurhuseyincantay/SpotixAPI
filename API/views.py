from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework import generics
from .models import *


class getAlbums(generics.ListAPIView):
    queryset = Album.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    def post(self,request):
        userId = request.POST.get("UserId")
        typeId = request.POST.get("TypeId")
        singer = Singer.objects.filter(id(userId))
        type = SongType.objects.filter(id(typeId))
        desc = request.POST.get("Description")
        albumCoverUrl = request.POST.get("AlbumCoverUrl")
        songcount =request.POST.get("songCount")
        # en son serializer ı post a ayarlayıp post için request atıyorduk 




