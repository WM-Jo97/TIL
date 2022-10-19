from rest_framework import serializers
from .models import Artist, Music

class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name',)

class MusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'title')

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist

class ArtistSerializer(serializers.ModelSerializer):
    comment_set = MusicListSerializer(many = True, read_only = True)
    comment_count = serializers.IntegerField(source = 'comment_set.count', read_only=True)
    class Meta:
        model = Artist
        fields = '__all__'


