from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.access.models import User


# Create your tests here.
class SignUpAPITests(APITestCase):
    def test_signup_valid_data(self):
        """Testcase for successful signup."""

        url = reverse("sign-up")
        data = {
            "email": "test@example.com",
            "username": "testuser",
            "first_name": "Vishnu",
            "last_name": "M",
            "password": "ValidPass1!",
            "confirm_password": "ValidPass1!",
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, "test@example.com")
        self.assertEqual(User.objects.get().username, "testuser")

    def test_signup_passwords_do_not_match(self):
        """Testcase for signup with passwords that do not match."""

        url = reverse("sign-up")
        data = {
            "email": "test@example.com",
            "username": "testuser",
            "first_name": "Vishnu",
            "last_name": "M",
            "password": "ValidPass1!",
            "confirm_password": "InvalidPass!",
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)
        self.assertIn("password", response.data["data"])  # Check that error is under confirm_password field
        self.assertEqual(response.data["data"]["password"][0], "Passwords do not match.")

    def test_signup_weak_password(self):
        """Testcase for signup with passwords that is weak."""

        url = reverse("sign-up")
        data = {
            "email": "test@example.com",
            "username": "testuser",
            "first_name": "Vishnu",
            "last_name": "M",
            "password": "weak",  # Too short, doesn't meet requirements
            "confirm_password": "weak",
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)
        self.assertIn("password", response.data["data"])  # Check that error is under password field
        self.assertEqual(response.data["data"]["password"][0], "Password must be at least 8 characters long.")

    def test_signup_password_with_no_digits(self):
        """Testcase for signup with passwords that have no single digit."""

        url = reverse("sign-up")
        data = {
            "email": "test@example.com",
            "username": "testuser",
            "first_name": "Vishnu",
            "last_name": "M",
            "password": "ValidPass!",
            "confirm_password": "ValidPass!",
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)
        self.assertIn("password", response.data["data"])  # Check that error is under password field
        self.assertEqual(response.data["data"]["password"][0], "Password must contain at least one digit.")

    def test_signup_password_with_no_upper_case(self):
        """Testcase for signup with passwords that have no upper case."""

        url = reverse("sign-up")
        data = {
            "email": "test@example.com",
            "username": "testuser",
            "first_name": "Vishnu",
            "last_name": "M",
            "password": "validpass1!",
            "confirm_password": "validpass1!",
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)
        self.assertIn("password", response.data["data"])  # Check that error is under password field
        self.assertEqual(response.data["data"]["password"][0], "Password must contain at least one uppercase letter.")

    def test_signup_password_with_no_special_char(self):
        """Testcase for signup with passwords that have no upper case."""

        url = reverse("sign-up")
        data = {
            "email": "test@example.com",
            "username": "testuser",
            "first_name": "Vishnu",
            "last_name": "M",
            "password": "ValidPass1",
            "confirm_password": "ValidPass1",
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)
        self.assertIn("password", response.data["data"])  # Check that error is under password field
        self.assertEqual(response.data["data"]["password"][0], "Password must contain at least one special character.")

    def test_signup_weak_username(self):
        """Testcase for weak username."""

        url = reverse("sign-up")
        data = {
            "email": "test@example.com",
            "username": "test",
            "first_name": "Vishnu",
            "last_name": "M",
            "password": "ValidPass1!",
            "confirm_password": "ValidPass1!",
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)
        self.assertIn("username", response.data["data"])  # Check that error is under username field
        self.assertEqual(response.data["data"]["username"][0], "Username must be at least 6 characters long.")

    def test_signup_email_in_use(self):
        """Testcase for signup with an email that is already in use."""

        User.objects.create_user(email="existing@example.com", password="ValidPass1!")
        url = reverse("sign-up")
        data = {
            "email": "existing@example.com",  # Already exists
            "username": "testuser",
            "first_name": "Vishnu",
            "last_name": "M",
            "password": "ValidPass1!",
            "confirm_password": "ValidPass1!",
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)  # Still only one user in database
        self.assertIn("email", response.data["data"])  # Check that error is under email field
