# 홈워크_db_08_hw01_P-1.py
# serializers.py

from rest_framework import serializers
from .models import Music


class MusicListSerializer(__(b)__):

    class Meta:
        model = Music
        fields = ("id", "title")