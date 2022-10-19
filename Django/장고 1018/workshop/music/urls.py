from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('artists/',views.artists_rc),
    path('artists/<int:artist_pk>', views.artists_g),
    path('artists/<int:artist_pk>/music/', views.artists_music),
    path('music/' , views.music)

]
