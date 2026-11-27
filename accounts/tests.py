from django.test import TestCase
from accounts.models import User
from rest_framework.test import APIRequestFactory
from types import SimpleNamespace
from permissions.role_permissions import IsAdminOrReadOnly, IsAdminOrAssignedEmployee

class UserModelTest(TestCase):

    def test_create_employee(self):
        user = User.objects.create_user(username="employee1", password="testpassword123")
        self.assertEqual(user.role, User.Role.EMPLOYEE)

    def test_create_admin(self):
        user = User.objects.create_user(username="admin", password="testpassword",role=User.Role.ADMIN)
        self.assertEqual(user.role, User.Role.ADMIN)

    def test_password_is_hashed(self):
        user = User.objects.create_user(username="employee2", password="testpassword123")

        self.assertNotEqual(user.password, "testpassword123")
        self.assertTrue(user.check_password("testpassword123"))
