from rest_framework.routers import DefaultRouter
from .viewset import BlogViewSet, CommentViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'posts', BlogViewSet)
router.register(r'comments', CommentViewSet)

