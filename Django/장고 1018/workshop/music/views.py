from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Artist, Music
from .serializers import ArtistListSerializer, ArtistSerializer, MusicListSerializer, MusicSerializer
from music import serializers


# Create your views here.

@api_view(['GET' , 'POST'])
def artists_rc(request):
    if request.method == 'GET':
        artists = get_list_or_404(Artist)
        serializer = ArtistListSerializer(artists, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArtistListSerializer(data = request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['GET'])
def artists_g(request, artist_pk):
    artist = get_object_or_404(Artist, pk = artist_pk)
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)    

@api_view(['POST'])
def artists_music(request):
    serializer = MusicListSerializer(data = request.data)
    if serializer.is_valid(raise_exception= True):
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

@api_view(['GET'])
def music(request):
    musics = Music.objects.all
    serializer = MusicListSerializer(musics)
    return Response(serializer.data, status.HTTP_201_CREATED)
