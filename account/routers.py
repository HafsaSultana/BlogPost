from rest_framework.routers import DefaultRouter
from . import viewset

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', viewset.UserViewSet)
