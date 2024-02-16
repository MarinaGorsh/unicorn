from django.urls import path
from .views import ResumeUpdateView, ResumeDetailView, ResumeCreateView


urlpatterns = [
    path("create/<str:username>", ResumeCreateView.as_view(), name="resume_create"),
    path("details/<str:username>", ResumeDetailView.as_view(), name="resume_detail"),
    path("update/<str:username>", ResumeUpdateView.as_view(), name="resume_update"),
]
