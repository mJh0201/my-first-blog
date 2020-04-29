#form model import, Post model import
from django import forms
from .models import Post

#만들 폼의 이름 PostForm 장고에 이 폼이 ModelForm 이라는 것을 알려줘야 한다.
#이를 위해 forms.ModelForm
class PostForm(forms.ModelForm):
    #이 폼을 만들기 위해 어떤 모델이 쓰여야 하는지 장고에 알려주는 구문 model = post
    class Meta:
        model = Post
        #title, text 만 보여지게 할 것.
        fields = ('title', 'text')
    