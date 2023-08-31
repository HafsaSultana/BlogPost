from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import BlogPostList, BlogPostDetails

urlpatterns = [
    path('blogs/', BlogPostList.as_view(), name='blogs_list'),
    path('blogs/<int:pk>/', BlogPostList.as_view(), name='blogs_details'),
]


