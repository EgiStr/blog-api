from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.filters import  SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

from .serializings import PostsSerializer,CreateSerializer,DetailSerializer
from .paginator import PostPagepaginator

from blog.models import Posts

class PostApiView(ListAPIView):
    serializer_class = PostsSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title','content','author__username']
    pagination_class = PostPagepaginator

    def get_queryset(self):
        query_Set = Posts.objects.all()
        return query_Set

class DetailApiView(RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'slug'

class DeleteApiView(DestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    lookup_field = 'slug'

class EditApiView(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    lookup_field = 'slug'

class MakeApiView(CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = CreateSerializer
    
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)
        return super().perform_create(serializer)