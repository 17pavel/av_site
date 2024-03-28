from django.urls import path

from .forms import save

app_name = 'users'

urlpatterns = [
    path('save/', save , name='answer'),
]