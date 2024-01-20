from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse, reverse_lazy


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to="media", null=True)

    def __str__(self) -> str:
        return self.email

    def get_absolute_url(self):
        return reverse("home")
