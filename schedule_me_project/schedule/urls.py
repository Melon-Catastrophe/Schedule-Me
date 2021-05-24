from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import PostListView, PostDetailView
from users.views import EventCreateView, EventUpdateView, EventDeleteView

from . import views as schedule_views

urlpatterns = [
    # path('', schedule_views.index, name='home'),
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', schedule_views.about, name='about'),
    path('scheduler/create/', EventCreateView.as_view(), name='event-create'),
    path('scheduler/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('scheduler/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
]