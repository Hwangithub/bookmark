from django.shortcuts import render

# Create your views here.
# CRUD(Create, Read, Update, Delete) : 웹 작업의 기초다.
#  - 웹에서는 이 CRUD 안에서 모든 기능이 돌아가게 된다.
# 이 네가지 페이지들을 장고에서 만들 수 있으면, 웬만한 사이트들은 다 만들 수 있다.
# 여기서는 먼저 LIST를 만들 것이다.

# 클래스형 뷰, 함수형 뷰가 있는데 / 클래스 뷰 : 상속받아서 사용하는 것이다.
# 클래스 뷰(제네릭 뷰)를 사용하려면, ListView를 하나 불러와야 한다.
from django.views.generic.list import ListView     # 장고인에 ListView가 있다
from  .models import Bookmark

class BookmarkListView(ListView):   # 장고안에 있는 'ListView'를 내려 받은 것이다.
    model = Bookmark

# 다음:
#  => config /urls.py로 가서, urlpatterns = [ ]에 넣어 주자.

