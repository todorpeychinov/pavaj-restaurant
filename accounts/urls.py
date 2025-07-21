from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include

from accounts import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', include(
         [
             path('profile-edit/', views.edit_profile, name='profile-edit'),
             path('profile-delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),

    ]
    )),
]