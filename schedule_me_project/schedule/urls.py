from django.urls import path

from . import views as schedule_views

urlpatterns = [
    path('', schedule_views.index, name='home'),
    path('about/', schedule_views.about, name='about'),
]