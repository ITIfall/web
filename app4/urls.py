from django.contrib import admin
from django.urls import path

from app4.views import indexView, postAnn, checkTitle, by_rubric, AnnDeleteView, AnnUpdateView

urlpatterns = [
    path('Friend/<int:pk>/update/', AnnUpdateView.as_view(), name='update'),
    path('Friend/<int:pk>/delete/', AnnDeleteView.as_view(), name='delete'),
    path('', indexView, name="index"),
    path('post/ajax/friend', postAnn, name="post_friend"),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('get/ajax/validate/nickname', checkTitle, name="validate_nickname")
]