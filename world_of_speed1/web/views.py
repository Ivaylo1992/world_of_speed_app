from django.shortcuts import render
from django.views import generic as views

from world_of_speed1.common.profile_helpers import GetProfileContextMixin


class IndexView(GetProfileContextMixin, views.TemplateView):
    template_name = "web/index.html"
