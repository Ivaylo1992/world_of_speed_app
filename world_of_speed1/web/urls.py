
from django.urls import path

from world_of_speed1.web import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]


