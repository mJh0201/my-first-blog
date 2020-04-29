from django.shortcuts import render
from .models import Post
#models.py 정의된 모델을 가져오기 위해 추가함. .의 의미는 현재 디렉토리 또는 애플리케이션을 의미
from django.utils import timezone
#
from django.shortcuts import render, get_object_or_404
#post new 뷰를 구현하기 위해 추가
from .forms import PostForm
#새 글을 작성한 다음에 post_detail 페이지로 이동할 수 있도록 하기 위해
from django.shortcuts import redirect

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

#Post new 뷰 구현
def post_new(request):
    if request.method == "POST":
        #폼에 입력된 데이터를 view 페이지로 가지고 올 때 받은 데이터를 PostForm으로 넘겨준다.
        form=PostForm(request.POST)
        # 폼에 들어있는 값들이 올바른지 체크
        if form.is_valid():
            #commit=False -> 넘겨진 데이터를 바로 Post 모델에 저장하지 말라는 뜻
            #작성자를 추가 한 뒤 저장해야 하므로
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            #저장
            post.save()
            #새 블로그 글을 작성한 뒤 바로 이동하면 좋겠죠?
            #이동해야 할 뷰(post_detail)로 바로 갈 수 있도록. post_detail 뷰는 pk필요
            return redirect('post_detail', pk=post.pk)
    else:
        #처음 페이지에 접속했을 때는 새 글을 쓸 수 있도록 폼이 비어있어야 한다.
        form=PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

#Post edit 할 수 있는 뷰 구현
#url로부터 추가로 pk 매개변수를 받아서 처리한다.
def post_edit(request, pk):
    #수정하고자 하는 글의 Post 모델 인스턴스로 가져온다. pk로 원하는 글을 찾는다.
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # 이전에 입력햇던 데이터가 있어야 한다. 수정하는 거니까?
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})