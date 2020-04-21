from django.contrib import admin
from .models import Todo  #같은 디렉토리인 models에서 Todo를 데려와라

# Register your models here. # 너의 모델을 넣어라 == todo 모델

admin.site.register(Todo)
