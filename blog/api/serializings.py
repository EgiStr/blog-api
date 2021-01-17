
from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField,SerializerMethodField
from blog.models import Posts
from comment.models import Comment
from comment.api.serializers import CommentChildSerializer

class PostsSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api:detail',
        lookup_field='slug' 
    )

    author = SerializerMethodField()
    category = SerializerMethodField()
    tags = SerializerMethodField()
    
    class Meta:
        model = Posts
        fields = [
            'url',
            'id',
            'author',
            'title',
            'thumb',
            'content',
            'category',
            'tags',
            'publish',

        ]

    def get_author(self,obj):
        return obj.author.username
    # obj = model it self or self in Posts
    def get_category(self,obj):
        return obj.category.content

    def get_tags(self,obj):
        post = obj.tags.names()
        return [t for t in post]

class DetailSerializer(ModelSerializer):
    author = SerializerMethodField()
    category = SerializerMethodField()
    tags = SerializerMethodField()
    comments = SerializerMethodField()
    
    class Meta:
        model = Posts
        fields =[
            'id',
            'author',
            'title',
            'content',
            'category',
            'thumb',
            'tags',
            'publish',
            'comments'
        ]
    

    def get_author(self,obj):
        return obj.author.username
    # obj = model it self or self in Posts
    def get_category(self,obj):
        return obj.category.content

    def get_tags(self,obj):
        post = obj.tags.names()
        return [t for t in post]

    def get_comments(self,obj):
        commets_qs = Comment.objects.filter_by_instance(obj)
        return CommentChildSerializer(commets_qs,many=True).data

class CreateSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields =[
            'title',
            'content',
            'publish',
            'category',
            'thumb'
        ]