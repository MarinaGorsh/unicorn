from django.urls import path
from .views import ResumeDetailView, ResumeCreateView


urlpatterns = [
    path("create/", ResumeCreateView.as_view(), name="resume_create"),
    path("details/<str:username>", ResumeDetailView.as_view(), name="resume_detail"),
]
