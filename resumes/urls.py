from django.urls import path
from .views import ResumeDetailView, ResumeCreateView


urlpatterns = [
    path(
        "resume/create/<str:username>", ResumeCreateView.as_view(), name="resume_create"
    ),
    path(
        "resume/detail/<str:username>", ResumeDetailView.as_view(), name="resume_detai"
    ),
]
