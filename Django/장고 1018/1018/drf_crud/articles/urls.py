from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('articles/', views.article_cr),
    path('articles/<int:article_pk>/', views.article_rud)
]