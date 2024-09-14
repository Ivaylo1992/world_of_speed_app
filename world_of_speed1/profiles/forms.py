from django import forms

from world_of_speed1.profiles.models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

        widgets = {
            "password": forms.PasswordInput()
        }


class CreateProfileForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        exclude = ("first_name", "last_name", "profile_picture")


class EditProfileForm(BaseProfileForm):
    ...