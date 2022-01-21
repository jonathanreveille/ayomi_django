import pytest
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


@pytest.mark.django_db
class TestUserApp(TestCase):

    def setUp(self):
        user = User.objects.create_user(username="jonathan",
                password="",
                email="test_ayomi@mail.com")
        user.set_password("ayomipasswordtest")
        user.save()
        self.client = Client()
        self.client.login(username="jonathan", password="ayomipasswordtest")

    def tearDown(self):
        return super().tearDown()

    def test_if_username_update_email(self):
        url = reverse('users:profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


