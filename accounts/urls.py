from django.urls import path

from accounts import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('profile-details/', views.profile_details, name='profile-details'),
    path('register/', views.register, name='register'),
]