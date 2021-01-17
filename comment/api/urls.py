
from django.urls import path
from .views import CommentList,EditCommentApi,DeleteCommentApiView
urlpatterns = [
    path("", CommentList.as_view(), name="index"),
    # path("detail/<slug:slug>", DetailApiView.as_view(), name="detail"),
    path("update/<int:pk>", EditCommentApi.as_view(), name="update"),
    path('delete/<int:pk>',DeleteCommentApiView.as_view(),name='delete'),
    # path('create',MakeApiView.as_view(),name='create'),
    # path('tags/<str:tag>',tagsList.as_view(),name='tag')
]
