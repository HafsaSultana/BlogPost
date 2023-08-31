from django.db.models import Q
from django.shortcuts import render
from .serializers import BlogPostSerializer
from .models import User, BlogPost
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.http import Http404
from django.contrib.auth import authenticate


class BlogPostList(APIView):
    pass


class BlogPostDetail(APIView):
    def get_object(self, pk):
        try:
            return BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            raise Http404

    def get(self, request, pk, formate=None):
        blog = self.get_object(pk)
        serializer = BlogPostSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk, formate=None):
        blog = self.get_object(pk)
        serializer = BlogPostSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







