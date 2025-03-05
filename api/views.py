from rest_framework import viewsets, permissions
from .models import Project, UserRole, Comment
from .serializers import ProjectSerializer, UserRoleSerializer, CommentSerializer
from django.contrib.auth.models import User

class IsOwnerOrEditor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return UserRole.objects.filter(user=request.user, project=obj, role__in=['owner', 'editor']).exists()

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrEditor]

    def perform_create(self, serializer):
        project = serializer.save()
        UserRole.objects.create(user=self.request.user, project=project, role='owner')

class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)