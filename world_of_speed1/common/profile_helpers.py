from world_of_speed1.profiles.models import Profile


class GetProfileContextMixin:
    extra_context = {
        "profile": Profile.objects.first()
    }


class GetProfileObjectMixin:
    def get_object(self, queryset=None):
        return Profile.objects.first()
