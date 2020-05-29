from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('about', views.about, name='about'),
    path('projects', views.project_list, name='project_list'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    path('accounts/', include('django.contrib.auth.urls')),

]

from django.conf.urls import url, include
from markdownx import urls as markdownx

urlpatterns += [
    url(r'^markdownx/', include(markdownx))
]