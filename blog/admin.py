from django.contrib import admin
from .models import Posts,Category
from comment.models import Comment
# Register your models here.
admin.site.register(Posts)
admin.site.register(Category)
admin.site.register(Comment)
