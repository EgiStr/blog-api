# Create your models here.

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
import json
from django.template.defaultfilters import slugify
from rest_framework.fields import JSONField
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    content = models.CharField(max_length=50)
    publish = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.content
    


class Posts(models.Model):

    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, default=3)
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True, null=True)
    publish = models.DateTimeField(auto_now=True, auto_now_add=False)
    update = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug= models.SlugField(blank=True, null=True)
    private = models.BooleanField(default =False)
    thumb = models.ImageField(upload_to='image/tumb', height_field='height_field', width_field='width_field',default='image/tumb/default.jpeg')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    tags = TaggableManager()

    class Meta:
        ordering=['-publish','-update']

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    @property
    def get_name_tags(self):
        tag= self.tags.values()
        return [t['name'] for t in tag]

    def save(self, *args, **kwargs):
       self.slug = slugify(self.title)
       super(Posts, self).save(*args, **kwargs) # Call the real save() method

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}.{}'.format(self.id,self.title)

    def __unicode__(self):
        return self.title
