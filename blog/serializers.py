from rest_framework import serializers
from .models import Blog, Comment


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'content_rich', 'image']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'blog', 'content', 'content_rich']

