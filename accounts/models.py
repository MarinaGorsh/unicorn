from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse, reverse_lazy
from django.apps import apps


# Create your models here.
class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to="pfps", null=True)
    name = models.TextField(default="", null=False, blank=False)
    email = models.EmailField()
    has_resume = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.email

    def get_absolute_url(self):
        return reverse("user_details", kwargs={"username": self.username})
