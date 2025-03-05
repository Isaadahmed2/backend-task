from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, UserRoleViewSet, CommentViewSet

# Create a router and register ViewSets
router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'roles', UserRoleViewSet)
router.register(r'comments', CommentViewSet)

# Define urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]