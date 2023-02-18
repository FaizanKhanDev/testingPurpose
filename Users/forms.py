from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.utils.translation import gettext_lazy as _

from Users.models import User


class HumsterSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    # api_key = forms.CharField(required=True)
    # api_secret = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)

        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        # user.api_key = self.cleaned_data.get('api_key')
        # user.api_secret = self.cleaned_data.get('api_secret')
        user.email = self.cleaned_data.get('email')
        user.save()

        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'balance_per', 'leverage', 'last_name', 'api_secret', 'api_key', 'trader']
