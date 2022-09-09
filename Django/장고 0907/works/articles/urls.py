from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    #path('new/',views.new, name = 'new'),
    path('create/', views.create, name = 'create'),
    path('index/', views.index, name = 'index' ),
    path('detail/<article_id>', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name= 'update'),
    path('<article_id>/delete/', views.delete, name='delete'),
]