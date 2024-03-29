from django.urls import path
from .views import (
    ResumeUpdateView,
    ResumeDetailView,
    ResumeCreateView,
    ResumeAccessForbidden,
)


urlpatterns = [
    path("create/<str:username>", ResumeCreateView.as_view(), name="resume_create"),
    path(
        "details/access-forbidden",
        ResumeAccessForbidden.as_view(),
        name="resume_access_forbidden",
    ),
    path("details/<str:username>", ResumeDetailView.as_view(), name="resume_details"),
    path("update/<str:username>", ResumeUpdateView.as_view(), name="resume_update"),
]
