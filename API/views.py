from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework import generics
from .models import *
from datetime import datetime

class getAlbums(generics.ListAPIView):
    queryset = Album.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    def post(self,request):
        singerId = request.POST.get("SingerId")
        typeId = request.POST.get("TypeId")
        singer = Singer.objects.get(pk=singerId)
        type = SongType.objects.get(pk=typeId)
        desc = request.POST.get("Description")
        albumCoverUrl = request.POST.get("AlbumCoverUrl")
        songcount =request.POST.get("songCount")
        dateString = request.POST.get("Date")
        datetime_object = datetime.strptime(dateString, '%m %d %Y')

        if singer is None:
            return Response((('Status', False), ('data', "No Singer Found")), status=status.HTTP_400_BAD_REQUEST)
        elif type is None:
            return Response((('Status', False), ('data', "No Type Found")), status=status.HTTP_400_BAD_REQUEST)
        elif datetime_object is None:
            return Response((('Status', False), ('data', "Date Type is not valid")), status=status.HTTP_400_BAD_REQUEST)
        album = Album(
            singer=singer,
            type=type,
            description=desc,
            song_count=songcount,
            album_cover=albumCoverUrl,
            release_date=datetime_object,
        )
        # en son obje check i yapıldıktan sonra database e save edilmesi gerekiyordu...
        serializer = AlbumSerializer(data=album.__dict__)
        if serializer.is_valid():
            serializer.create(album)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




