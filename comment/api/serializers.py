
from django.http import request
from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField,SerializerMethodField
from comment.models import Comment

class CommentSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='apicomment:update',
        lookup_field='pk'
    )
    user= SerializerMethodField()
    repliesCount = SerializerMethodField()
    
    class Meta:
        model = Comment
        fields= [
            'url',
            'id',
            'user',
            'contenttype',
            'object_id',
            'parent' ,
            'content',
            'timestamp',
            'repliesCount',
           
        ]

    def get_user(self,obj):
        return obj.user.username

    def get_repliesCount(self,obj):
        return obj.children().count()

class CommentChildSerializer(ModelSerializer):
    replies = SerializerMethodField()
    user = SerializerMethodField()
    class Meta:
        model = Comment
        fields= [

            'id',
            'user',
            'contenttype',
            'object_id',
            'content',
            'timestamp',
            'parent',
            'replies',
            
        ]
    def get_replies(self,obj):    
        return CommentChildSerializer(obj.children(),many=True).data
    
    def get_user(self,obj):
        return obj.user.username