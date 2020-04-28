#다른 파일에 있는 부분 추가로 불러옴
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
#Class Post(models.Model): 모델을 정의하는 코드 모델은 객체
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publiched_date = models.DateTimeField(blank = True, null = True)

    def publich(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
