from django.urls import path, include
from world_of_speed1.cars import views

urlpatterns = [
    path('catalogue/', views.CatalogueCarView.as_view(), name="catalogue_car"),
    path('create/', views.CreateCarView.as_view(), name="create_car"),
    path("<int:id>/", include([
        path("details/", views.DetailsCarView.as_view(), name="details_car"),
        path("edit/", views.EditCarView.as_view(), name="edit_car"),
        path("delete/", views.DeleteCarView.as_view(), name="delete_car"),
    ]))
]