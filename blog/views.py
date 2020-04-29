from django.shortcuts import render

# Create your views here.
#요청을 넘겨 받아 render 메서드 호출하고 받은 return blog/post_list.html 템플릿을 보여즘
def post_list(request):
    return render(request, 'blog/post_list.html', {})
