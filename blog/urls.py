from django.urls import path
from .views import *

### BLOG URL

urlpatterns = [
    path('', post_list, name='home'),
    path('<str:slug>/', post_details, name='post_detail'),
]
