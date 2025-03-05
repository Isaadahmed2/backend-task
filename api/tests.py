from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project, UserRole, Comment

class ProjectTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.project = Project.objects.create(name='Test Project', description='Test Description')

    def test_project_creation(self):
        self.assertEqual(self.project.name, 'Test Project')

    def test_user_role_creation(self):
        UserRole.objects.create(user=self.user, project=self.project, role='owner')
        self.assertEqual(UserRole.objects.count(), 1)