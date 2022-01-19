from django.contrib import admin
from django.urls import path

from app4.views import indexView, postFriend, checkNickName, by_rubric, FriendDeleteView, FriendUpdateView

urlpatterns = [
    path('Friend/<int:pk>/update/', FriendUpdateView.as_view(), name='update'),
    path('Friend/<int:pk>/delete/', FriendDeleteView.as_view(), name='delete'),
    path('', indexView, name="index"),
    path('post/ajax/friend', postFriend, name="post_friend"),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('get/ajax/validate/nickname', checkNickName, name="validate_nickname")
]