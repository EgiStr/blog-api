from django import forms
from django.shortcuts import render, get_object_or_404,redirect

from django.views.generic import ListView, DetailView
from .models import Posts
from comment.models import Comment
from .forms import postForm
from comment.forms import CommetForm
# Create your views here.

class PostsListView(ListView):
    model = Posts
    template_name = "blog/index.html"
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        common_tags = Posts.tags.most_common()[:4]
        context["common_tags"] = common_tags
        return context

class PostsDetailView(DetailView):
    model = Posts
    template_name = "blog/detail.html"
    context_object_name= 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        instance = get_object_or_404(Posts,slug=slug)
        comment = Comment.objects.filter_by_instance(instance)
        form = CommetForm()
        context["comments"]= comment
        context['form']= form 
        return context
    def post(self,request,*args, **kwargs):
        slug = self.kwargs['slug']
        instance = get_object_or_404(Posts, slug=slug)

        form = CommetForm(self.request.POST)

        if form.is_valid():
            data = form.save()
            data.contenttype = instance.get_content_type
            data.object_id = instance.id
            data.user = request.user
            parent_obj = None
            try:
                parent_id = int(request.POST['parent_id'])
            except:
                parent_id = None
            if parent_id:
                parent_qs = Comment.objects.filter(id=parent_id)
                if parent_qs.exists() and parent_qs.count() == 1:
                    parent_obj = parent_qs.first()

            data.parent = parent_obj
            data.save()

            self.object = self.get_object()
            context = super(DetailView, self).get_context_data(**kwargs)
            form = CommetForm()
            comments = Comment.objects.filter_by_instance(instance)
            context['comments'] = comments
            context['form'] = form
            return self.render_to_response(context=context)
        else:
            print('error')


def PostCreate(request):
    form = postForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            data = form.save()
            data.author = request.user
            data.save()
            return redirect('blog:detail', slug=data.slug)
        else:
            error = True
            context = {
                'form': form,
                'error': error,
            }
            return render(request, 'blog/create.html', context)
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)

class tagsList(ListView):
    model = Posts
    template_name = 'blog/taslist.html'
    context_object_name = 'posts'

    def get_queryset(self,*args, **kwargs):
        get_par = self.kwargs['tag']
        qs = self.model.objects.filter(tags__name__in=[get_par])
        # self.get_queryset = self.model.objects.filter(tags__name__in=[get_par]).annotate(num_tags=Count('tags'))[0]
        self.queryset = qs
        return super().get_queryset()
    