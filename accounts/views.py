from django.contrib.auth import get_user_model, login, authenticate
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import AppUserCreationForm

UserModel = get_user_model()


# Create your views here.


def profile_details(request):
    return render(request, 'accounts/profile-details.html')


class RegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Note: Signal for profile creation

        if response.status_code in [301, 302]:
            user = authenticate(
                self.request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            if user is not None:
                login(self.request, user)

        return response
