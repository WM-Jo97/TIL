from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('lotto/' , views.lotto, name='lotto'), #해당 경로의 이름을 lotto라고 정의
    path('index/' , views.index, name='index'),
    #Variable routing 사용 시 주의점!
    # 1. 변수명과 views.py의 함수 매개변수의 이름이 같아야한다.
    # 2. Variable routing 이 설정되면 반드시 매개변수로 받아야 한다.
    # 3. Variable routing이 적용된 주소에는 반드시 값이 들어가 있어야 한다.
    path('hello/<name>/<int:age>/',views.hello, name='hello'),
    
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    
    path('detail/<post_id>', views.detail, name='detail'),
    
    # 글 수정을 위한 edit, update
    path('edit/<post_id>', views.edit, name = 'edit'),
    path('update/<post_id>', views.update, name='update'),

    # 글 삭제를 위한 delete
    path('delete/<post_id>', views.delete, name='delete')
    ]
