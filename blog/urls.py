
from django.urls import path
from .views import PostsListView,PostsDetailView,PostCreate,tagsList

urlpatterns = [
    path("", PostsListView.as_view(), name="index"),
    path("detail/<slug:slug>", PostsDetailView.as_view(), name="detail"),
    path('create',PostCreate,name='create'),
    path('tags/<str:tag>',tagsList.as_view(),name='tag')
]
