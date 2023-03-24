from django.urls import path
from .views import BookmarkListView
# from .views import *

urlpatterns = [

         # http://127.0.0.1/bookmark/
         # path에 ""가 있는 것은 bookmark까지(위 주소)를 담고 있다는 것을 의미
    path("", BookmarkListView.as_view(), name='list'),

]