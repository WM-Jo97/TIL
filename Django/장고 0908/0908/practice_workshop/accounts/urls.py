from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup , name = 'signup'),
    path('login/', views.login , name = 'login'),
    path('logout/', views.logout , name = 'logout'),
    path('index/', views.index , name = 'index'),
    path('update/', views.update, name = 'update'),
    path('delete/', views.delete, name = 'delete'),
    path('login_index', views.login_index, name = 'login_index'),
    path('password/', views.password, name = 'password'),
]