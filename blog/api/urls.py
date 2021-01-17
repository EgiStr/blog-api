
from django.urls import path
from .views import PostApiView,DetailApiView,DeleteApiView,EditApiView,MakeApiView

urlpatterns = [
    path("", PostApiView.as_view(), name="index"),
    path("detail/<slug:slug>", DetailApiView.as_view(), name="detail"),
    path("update/<slug:slug>", EditApiView.as_view(), name="update"),
    path('delete/<slug:slug>',DeleteApiView.as_view(),name='delete'),
    path('create',MakeApiView.as_view(),name='create'),
    # path('tags/<str:tag>',tagsList.as_view(),name='tag')
]
