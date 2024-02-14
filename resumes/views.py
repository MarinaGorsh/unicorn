from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from .models import Resume
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.apps import apps


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
        return not Resume.objects.filter(owner=self.request.user)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.owner = self.request.user
        self.request.user.has_resume = True
        return super().form_valid(form)


class ResumeDetailView(DetailView):
    model = Resume
    template_name = "resume_detail.html"

    def get_object(self, queryset=None) -> Model:
        if not queryset:
            queryset = super().get_queryset()
        return queryset.get(owner__username=self.kwargs["username"])
