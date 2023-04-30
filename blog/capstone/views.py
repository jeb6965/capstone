from django.views import generic
from .models import Post
from django.views.generic import TemplateView
# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    
class Aboutme(TemplateView):
    template_name = 'aboutme.html'
    
class Thesis(TemplateView):
    template_name = 'thesis.html'
    
class Myjourney(TemplateView):
    template_name = 'myjourney.html'
    
class Reflection(TemplateView):
    template_name = 'reflection.html'