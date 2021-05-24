from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView

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
    event_list = Event.objects.all().filter(creator=request.user.id).order_by('day', 'time')
    sundays = Event.objects.all().filter(creator=request.user.id, day__contains='Sunday').order_by('time')
    mondays = Event.objects.all().filter(creator=request.user.id, day__contains='Monday').order_by('time')
    tuesdays = Event.objects.all().filter(creator=request.user.id, day__contains='Tuesday').order_by('time')
    wednesdays = Event.objects.all().filter(creator=request.user.id, day__contains='Wednesday').order_by('time')
    thursdays = Event.objects.all().filter(creator=request.user.id, day__contains='Thursday').order_by('time')
    fridays = Event.objects.all().filter(creator=request.user.id, day__contains='Friday').order_by('time')
    saturdays = Event.objects.all().filter(creator=request.user.id, day__contains='Saturday').order_by('time')
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

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'time', 'day']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(EventCreateView, self).form_valid(form)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'time', 'day']
    template_name = 'schedule/event_update.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.creator
        # if self.request.user == event.creator:
        #     return True
        # return False


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url='/scheduler/'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.creator:
            return True
        return False

    
@login_required
def event_day(request, day):
    event_list = Event.objects.all().filter(day__contains=day, creator=request.user.id).order_by('time')
    context = {
        'events': event_list,
        'day': day,
    }
    return render(request, 'schedule/event_day.html', context)
