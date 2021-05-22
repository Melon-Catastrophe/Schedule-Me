from django.shortcuts import render
from .models import Post, Event

def index(request):
    latest_post_list = Post.objects.order_by('-date_posted')
    context = {
        'title': 'Schedule Me | Home',
        'posts': latest_post_list,

    }

    return render(request, 'schedule/home.html', context)
    # The second parameter for the render function should be in this format (I believe): 'app_name/html_name'


def about(request):
    return render(request, 'schedule/about.html', {'title': 'Schedule Me | About'})


