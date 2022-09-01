from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('article/',views.index , name='index')
    
]
