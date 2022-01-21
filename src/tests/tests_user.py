import pytest
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from users.forms import UserUpdateForm

@pytest.mark.django_db
class TestUserApp(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="jonathan",
                password="",
                email="test_ayomi@mail.com")
        self.user.set_password("ayomipasswordtest")
        self.user.save()
        self.client = Client()
        self.client.login(username="jonathan", password="ayomipasswordtest")

    def tearDown(self):
        return super().tearDown()

    def test_views(self):
        url = reverse('users:logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        url = reverse('users:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_if_username_update_email(self):
        url = reverse('users:profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # if user changes email with the form
        request = self.client.post(url, {'email':'new_random_email@test.com'})
        self.assertEqual(request.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email,  "new_random_email@test.com")
