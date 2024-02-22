from django.urls import path
from .views import (
    CustomUserUpdateView,
    SignUpView,
    CustomUserDetailView,
    ProfilePictureUpdateView,
    UserNotFoundView,
)


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path(
        "change_info/<str:username>", CustomUserUpdateView.as_view(), name="user_change"
    ),
    path(
        "change_profile_picture/<str:username>",
        ProfilePictureUpdateView.as_view(),
        name="user_change_profile_picture",
    ),
    path("details/<str:username>", CustomUserDetailView.as_view(), name="user_details"),
    path("not-found/", UserNotFoundView.as_view(), name="user_not_found"),
]
