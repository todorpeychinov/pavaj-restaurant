from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from accounts import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('profile-details/', views.profile_details, name='profile-details'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]