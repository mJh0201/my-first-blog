from django.shortcuts import render
from .models import Post
#models.py 정의된 모델을 가져오기 위해 추가함. .의 의미는 현재 디렉토리 또는 애플리케이션을 의미
from django.utils import timezone
#
from django.shortcuts import render, get_object_or_404

# Create your views here.
#요청을 넘겨 받아 render 메서드 호출하고 받은 return blog/post_list.html 템플릿을 보여즘

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

#Post 상세 페이지 내부 뷰 추가
def post_detail(request,pk):
    #pk에 해당하는 post 가 없을 경우 404 error 띄워 줌
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})