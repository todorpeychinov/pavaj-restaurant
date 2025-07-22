from django.urls import path

from common import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('main-menu/', views.MenuListView.as_view(), name='main-menu'),
    path('seasonal-menu/', views.SeasonalMenuListView.as_view(), name='seasonal-menu'),
    path('wine-list/', views.WineListView.as_view(), name='wine-list'),

]