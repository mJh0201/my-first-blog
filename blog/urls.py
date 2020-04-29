from django.urls import path
from . import views

#기존의 url에서 상세 페이지를 만들기 위해 추가한다.
# urlpatterns = [path('', views.post_list, name='post_list'), ]

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]