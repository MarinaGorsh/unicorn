from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser

class HomeViewTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Welcome to Unicorn AI!")
        self.assertContains(response, "Log in")
        self.assertContains(response, "Search profiles:")
        self.assertContains(response, "Username:")

class ResumeCreateViewTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='user', password='password')

    def test_user_change_and_resume_create(self):
        self.client.login( username='user', password='password')
        response = self.client.get(reverse("user_change", args=["user"]))
        self.assertContains(response, "Change info")
        response2 = self.client.get(reverse("resume_create", args=["user"]))
        self.assertContains(response2, "Create resume")
