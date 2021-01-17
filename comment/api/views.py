import rest_framework

from rest_framework.mixins import DestroyModelMixin,UpdateModelMixin
from rest_framework.generics import ListAPIView,DestroyAPIView,RetrieveAPIView
from comment.models import Comment
from .serializers import CommentSerializer,CommentChildSerializer

class CommentList(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()
    
class EditCommentApi(RetrieveAPIView,DestroyModelMixin,UpdateModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentChildSerializer

    def put(self,request,*args, **kwargs):
        self.update(request,*args, **kwargs)
        
    def delete(self,request,*args, **kwargs):
        self.destroy(request,*args, **kwargs)


class DeleteCommentApiView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer