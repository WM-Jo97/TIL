from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('article/', views.article_cr),
    path('article/<int:article_pk>' , views.article_ru),
    
]