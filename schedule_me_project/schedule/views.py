from django.shortcuts import render
from .models import Post

def index(request):
    context = {
        'title': 'Schedule Me | Home',
        'posts': Post.objects.all(),
    }

    return render(request, 'schedule/home.html', context)
    # The second parameter for the render function should be in this format (I believe): 'app_name/html_name'


def about(request):
    return render(request, 'schedule/about.html', {'title': 'Schedule Me | About'})
