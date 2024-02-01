from django.urls import path
from .views import (
    CustomUserChangeView,
    SignUpView,
    CustomUserDetailView,
    ProfilePictureChangeView,
)


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path(
        "change_info/<str:username>", CustomUserChangeView.as_view(), name="user_change"
    ),
    path(
        "change_profile_picture/<str:username>",
        ProfilePictureChangeView.as_view(),
        name="user_change_profile_picture",
    ),
    path("details/<str:username>", CustomUserDetailView.as_view(), name="user_detail"),
]
