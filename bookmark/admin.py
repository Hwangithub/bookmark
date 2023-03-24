from django.contrib import admin

# Register your models here.
# 내가 만든 모델을 관리자 페이지에서 관리하도록 등록하자
from .models import Bookmark

admin.site.register(Bookmark)
# 서버를 실행해서 관리자 페이지에 가서 내용을 보자