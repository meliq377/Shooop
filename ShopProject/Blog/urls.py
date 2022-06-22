from django.urls import path
from .views import *

app_name = 'Blog'

urlpatterns = [
    path('', post_list, name='post_list')
]