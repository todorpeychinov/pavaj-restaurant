from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileEditForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ['user']


class UserBaseForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'


class UserEditForm(UserBaseForm):
    class Meta(UserBaseForm.Meta):
        fields = ['first_name', 'last_name']
