from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Custom_user


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Custom_user
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Custom_user
        fields = ("email",)