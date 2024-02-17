import email
from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from .forms import CustomUserCreationForm
from .models import CustomUser


# Create your views here.
class SignUpView(CreateView):
    template_name = "signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")


class CustomUserUpdateView(UpdateView):
    model = CustomUser
    template_name = "user_update.html"
    fields = ["name"]

    def get_object(self, queryset=None) -> CustomUser:
        return CustomUser.objects.get(username=self.kwargs["username"])


class ProfilePictureUpdateView(UpdateView):
    model = CustomUser
    template_name = "update_profile_picture.html"
    fields = ["profile_picture"]

    def get_object(self, queryset=None) -> CustomUser:
        return CustomUser.objects.get(username=self.kwargs["username"])


class CustomUserDetailView(UserPassesTestMixin, DetailView):
    model = CustomUser
    template_name = "user_detail.html"

    def get_object(self, queryset=None) -> CustomUser:
        return CustomUser.objects.get(username=self.kwargs["username"])

    # Check if user is allowed to view resume
    def test_func(self) -> bool:
        return bool(
            self.request.user.is_authenticated
            or CustomUser.objects.get(
                username=self.kwargs["username"]
            ).let_anon_users_see_resume
        )


class UserNotFoundView(TemplateView):
    template_name = "user_not_found.html"
