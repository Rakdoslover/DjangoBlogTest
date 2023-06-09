from . import views
from django.urls import path
from .forms import CommentForm

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path(
        'choiceone/<slug:slug>',
        views.PostChoiceOne.as_view(), name='post_choice_one'
    ),
]
