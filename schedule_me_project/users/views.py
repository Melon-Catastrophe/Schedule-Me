from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import UserRegisterForm
from schedule.models import Event

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')    # This .get is a dictionary. In this context, it looks for the value that matches the key 'username'.
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required     # A decorator that adds the login be required to visit this view.
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def scheduler(request):
    event_list = Event.objects.all().filter(creator=request.user.id).order_by('day', '-time')
    sundays = Event.objects.all().filter(creator=request.user.id, day__contains='Sunday').order_by('day', '-time')
    mondays = Event.objects.all().filter(creator=request.user.id, day__contains='Monday').order_by('day', '-time')
    tuesdays = Event.objects.all().filter(creator=request.user.id, day__contains='Tuesday').order_by('day', '-time')
    wednesdays = Event.objects.all().filter(creator=request.user.id, day__contains='Wednesday').order_by('day', '-time')
    thursdays = Event.objects.all().filter(creator=request.user.id, day__contains='Thursday').order_by('day', '-time')
    fridays = Event.objects.all().filter(creator=request.user.id, day__contains='Friday').order_by('day', '-time')
    saturdays = Event.objects.all().filter(creator=request.user.id, day__contains='Saturday').order_by('day', '-time')
    context = {
        'events': event_list,
        'sundays': sundays,
        'mondays': mondays,
        'tuesdays': tuesdays,
        'wednesdays': wednesdays,
        'thursdays': thursdays,
        'fridays': fridays,
        'saturdays': saturdays,
    }
    return render(request, 'users/scheduler.html', context)
    
@login_required
def event_day(request, day):
    event_list = Event.objects.all().filter(day__contains=day, creator=request.user.id)
    context = {
        'events': event_list,
        'day': day,
    }
    return render(request, 'schedule/event_day.html', context)
