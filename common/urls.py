from django.urls import path

from common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('main-menu/', views.main_menu, name='main-menu'),
    path('seasonal-menu/', views.seasonal_menu, name='seasonal-menu'),
    path('wine-list/', views.wine_list, name='wine-list'),
    path('confirm-delete/', views.confirmation_page, name='confirm-delete'),
]