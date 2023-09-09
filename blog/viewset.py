from rest_framework import viewsets

from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Blog
from .serializers import BlogSerializer,CommentSerializer


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class=BlogSerializer
    permission_classes = [AllowAny]
    queryset=Blog.objects.all()
    


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class=CommentSerializer
    queryset=Blog.objects.all()