from django.conf.urls import url
from django.urls import path

import compare
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^search/$', compare.views.search_titles)
]