from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from .models import Resume
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class ResumeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Resume
    template_name = "resume_create.html"

    def test_func(self) -> bool:
        return not self.request.user.has_resume()

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ResumeDetailView(DetailView):
    model = Resume
    template_name = "resume_detail.html"

    def get_object(self, queryset) -> Resume:
        return Resume.objects.get(owner=self.kwargs["username"])
