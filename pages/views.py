from django.http import (
    HttpResponseBadRequest,
    HttpResponseNotAllowed,
    HttpResponseNotFound,
)
from django.shortcuts import redirect, render
from django.views import View, generic
from .forms import UserSearchForm
from django.apps import apps


# Create your views here.
class HomeView(View):
    template_name = "home.html"
    form_class = UserSearchForm

    def get(self, request, *args, **kwargs):
        user_search_form = self.form_class()
        context = {"user_search_form": user_search_form}

        return render(request, "home.html", context)

    def post(self, request, *args, **kwargs):
        submitted_form = self.form_class(self.request.POST)

        # Check if submitted form is valid
        if not submitted_form.is_valid():
            print("Not valid")
            return HttpResponseBadRequest()

        if "username" in submitted_form.cleaned_data:
            searched_username = submitted_form.cleaned_data["username"]
        else:
            print("No username")
            print(submitted_form.cleaned_data)
            return HttpResponseBadRequest()

        # Show searched user if exists
        if (
            apps.get_model("accounts", "CustomUser")
            .objects.filter(username=searched_username)
            .exists()
        ):
            return redirect("user_details", searched_username)
        else:
            return HttpResponseNotFound()
