# 홈워크_db_08_hw01_P-2.py
# views.py

from .serializers import __(a)__
from rest_framework.response import __(d)__


@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = __(a)__(musics, __(c)__)
    return __(d)__(serializer.__(e)__)