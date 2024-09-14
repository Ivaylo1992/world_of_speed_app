from django import forms

from world_of_speed1.cars.models import Car


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        exclude = ("owner", )
        widgets = {
            "image_url": forms.URLInput(
                attrs={
                    "placeholder": "https://..."
                }
            )
        }


class CreateCarForm(BaseCarForm):
    class Meta(BaseCarForm.Meta):
        ...


class EditCarForm(BaseCarForm):
    class Meta(BaseCarForm.Meta):
        ...


class DeleteCarForm(BaseCarForm):

    def __init__(self, *args, **kwargs):
        super(DeleteCarForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["readonly"] = "readonly"
            # self.fields[field].widget.attrs["disabled"] = "disabled"

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance