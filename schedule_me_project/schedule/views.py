from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Event

def index(request):
    latest_post_list = Post.objects.order_by('-date_posted')
    context = {
        'title': 'Schedule Me | Home',
        'posts': latest_post_list,

    }

    return render(request, 'schedule/home.html', context)
    # The second parameter for the render function should be in this format (I believe): 'app_name/html_name'


class PostListView(ListView):
    model = Post
    template_name = 'schedule/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    



def about(request):
    return render(request, 'schedule/about.html', {'title': 'Schedule Me | About'})


