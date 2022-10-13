from django import forms
from .models import Article, Comment

# class ArticleForm(forms.Form):
#     REGION_A = 'sl'
#     REGION_B = 'dj'
#     REGION_C = 'gj'
#     REGION_D = 'gm'
#     REGION_E = 'bs'
#     REGIONS_CHOICES = [
#         (REGION_A, '서울'),
#         (REGION_B, '대전'),
#         (REGION_C, '광주'),
#         (REGION_D, '구미'),
#         (REGION_E, '부산'),
#     ]
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea())
#     region = forms.ChoiceField(choices=REGIONS_CHOICES, widget=forms.Select())

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title', 
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': 'Please enter your content'
        }
    )
    
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ('author',)


class CommentForm(forms.ModelForm):
    '''
    게시글을 조회했을 때 (detail) 댓글을 다는 것이 일반적임
    그래서 게시글의 detail 에서 CommentForm을 사용해서
    유저들이 작성할 수 있도록 해야함
    '''
    class Meta:
        model = Comment
        fields = ('content',)
