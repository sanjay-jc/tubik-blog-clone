from django.urls import path
from .views import *


urlpatterns =[
    path('',home,name='homepage'),
    path('all-category',all_category,name='all_category'),
]