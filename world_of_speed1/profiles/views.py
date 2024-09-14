from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from world_of_speed1.common.profile_helpers import GetProfileObjectMixin
from world_of_speed1.profiles.forms import CreateProfileForm, EditProfileForm
from world_of_speed1.profiles.models import Profile


class DetailsProfileView(GetProfileObjectMixin, views.DetailView):
    model = Profile
    template_name = "profiles/profile-details.html"


class EditProfileView(GetProfileObjectMixin, views.UpdateView):
    model = Profile
    template_name = "profiles/profile-edit.html"
    form_class = EditProfileForm
    success_url = reverse_lazy("details_profile")


class CreateProfileView(views.CreateView):
    model = Profile
    template_name = "profiles/profile-create.html"
    success_url = reverse_lazy("index")
    form_class = CreateProfileForm


class DeleteProfileView(GetProfileObjectMixin, views.DeleteView):
    queryset = Profile.objects.all()
    template_name = "profiles/profile-delete.html"
    success_url = reverse_lazy("index")

