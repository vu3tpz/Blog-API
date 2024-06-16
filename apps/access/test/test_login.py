from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.access.models import User


class LoginAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@example.com", password="ValidPass1!", type="user")
        self.url = reverse("login")

    def test_login_valid_credentials(self):
        data = {"email": "test@example.com", "password": "ValidPass1!", "type": "user"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data["data"])

    def test_login_invalid_password(self):
        data = {"email": "test@example.com", "password": "InvalidPass!", "type": "user"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Please check your login credentials.", response.data["data"])

    def test_login_invalid_type(self):
        data = {"email": "test@example.com", "password": "ValidPass1!", "type": "invalid"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Please check your login credentials.", response.data["data"])

    def test_login_user_not_found(self):
        data = {"email": "nonexistent@example.com", "password": "ValidPass1!", "type": "user"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Please check your login credentials.", response.data["data"])
