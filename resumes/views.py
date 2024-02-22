from typing import Any
from django.apps import apps
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView
from .models import Resume
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class ResumeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Resume
    template_name = "resume_create.html"
    fields = [
        "job_title",
        "skills",
        "languages",
        "about",
        "experience",
        "let_anon_users_see_resume",
    ]

    def test_func(self) -> bool:
        return not Resume.objects.filter(
            owner__username=self.kwargs["username"]
        ).exists()

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.owner = self.request.user
        self.request.user.has_resume = True
        self.request.user.save()
        return super().form_valid(form)


class ResumeDetailView(UserPassesTestMixin, DetailView):
    model = Resume
    template_name = "resume_details.html"

    def test_func(self) -> bool:
        """
        Checks if user is either authentificated or is let to view anonymously
        """

        return (
            self.request.user.is_authenticated
            or Resume.objects.get(
                owner__username=self.kwargs["username"]
            ).let_anon_users_see_resume
        )

    def handle_no_permission(self) -> HttpResponseRedirect:
        return redirect("resume_access_forbidden")

    def get_object(self) -> Resume:
        return Resume.objects.get(owner__username=self.kwargs["username"])


class ResumeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Resume
    template_name = "resume_update.html"
    fields = [
        "job_title",
        "skills",
        "languages",
        "about",
        "experience",
        "let_anon_users_see_resume",
    ]

    def get_object(self, queryset=None) -> Resume:
        if not queryset:
            queryset = super().get_queryset()

        return Resume.objects.get(owner__username=self.kwargs["username"])

    def test_func(self) -> bool:
        # Check if resume exists
        if not Resume.objects.filter(owner__username=self.kwargs["username"]).exists():
            return False

        # Check if user is the owner
        return (
            self.request.user
            == Resume.objects.get(owner__username=self.kwargs["username"]).owner
        )


class ResumeAccessForbidden(TemplateView):
    template_name = "resume_access_forbidden.html"
