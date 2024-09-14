from django.urls import reverse_lazy
from django.views import generic as views

from world_of_speed1.cars.forms import CreateCarForm, EditCarForm, DeleteCarForm
from world_of_speed1.cars.models import Car
from world_of_speed1.common.profile_helpers import GetProfileContextMixin
from world_of_speed1.profiles.models import Profile


class EditCarView(GetProfileContextMixin, views.UpdateView):
    queryset = Car.objects.all()
    template_name = "cars/car-edit.html"
    form_class = EditCarForm
    success_url = reverse_lazy("catalogue_car")

    context_object_name = "car"
    pk_url_kwarg = "id"


class DeleteCarView(views.DeleteView):
    queryset = Car.objects.all()
    template_name = "cars/car-delete.html"
    success_url = reverse_lazy("catalogue_car")
    form_class = DeleteCarForm

    pk_url_kwarg = "id"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs


class CatalogueCarView(GetProfileContextMixin, views.ListView):
    queryset = Car.objects.all()
    template_name = "cars/catalogue.html"


class CreateCarView(GetProfileContextMixin, views.CreateView):
    queryset = Car.objects.all()
    template_name = "cars/car-create.html"
    form_class = CreateCarForm
    success_url = reverse_lazy("catalogue_car")

    def form_valid(self, form):
        form.instance.owner = Profile.objects.firts()
        return super().form_valid(form)


class DetailsCarView(GetProfileContextMixin, views.DetailView):
    queryset = Car.objects.all()
    template_name = "cars/car-details.html"
    context_object_name = "car"

    pk_url_kwarg = "id"
