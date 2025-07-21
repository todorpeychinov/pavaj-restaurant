from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from accounts.forms import AppUserCreationForm, ProfileEditForm, UserEditForm
from accounts.models import Profile

UserModel = get_user_model()


# Create your views here.


def profile_details(request):
    return render(request, 'accounts/profile-edit.html')


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


@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    user = request.user

    user_form = UserEditForm(request.POST or None, instance=user)
    profile_form = ProfileEditForm(request.POST or None, instance=profile)

    if request.method == 'POST' and user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        return redirect('profile-edit')

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'accounts/profile-edit.html', context)


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/delete-profile-confirmation-page.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user
