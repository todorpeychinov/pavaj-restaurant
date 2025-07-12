from django.shortcuts import render

from accounts.forms import LoginForm


# Create your views here.

def login(request):
    form = LoginForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def profile_details(request):
    return render(request, 'accounts/profile-details.html')


def register(request):
    return render(request, 'accounts/register.html')
