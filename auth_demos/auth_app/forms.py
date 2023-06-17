from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from auth_app.models import Profile

UserModel = get_user_model()
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            user=user,
        )
        if commit:
            profile.save()
        profile.save()
        return user





