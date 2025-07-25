from django.urls import path

from rest_api import views

urlpatterns = [
    path('menu/', views.MenuAPIView.as_view(), name="menu-api"),
]
