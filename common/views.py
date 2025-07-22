from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from menu.models import MenuItem


# Create your views here.
class IndexView(TemplateView):
    template_name = 'common/index.html'


class AboutView(TemplateView):
    template_name = 'common/about.html'


class ContactView(TemplateView):
    template_name = 'common/contact.html'


class MenuListView(ListView):
    model = MenuItem
    template_name = 'common/main-menu.html'
    context_object_name = 'menu_items'

    def get_queryset(self):
        return (
            MenuItem.objects.select_related('category')
            .filter(category__menu_type__ncode='100')
            .order_by('category__order', 'name')
        )


class SeasonalMenuListView(ListView):
    model = MenuItem
    template_name = 'common/seasonal-menu.html'
    context_object_name = 'menu_items'

    def get_queryset(self):
        return (
            MenuItem.objects.select_related('category')
            .filter(category__menu_type__ncode='200')
            .order_by('category__order', 'name')
        )


class WineListView(ListView):
    model = MenuItem
    template_name = 'common/wine-list.html'
    context_object_name = 'menu_items'

    def get_queryset(self):
        return (
            MenuItem.objects.select_related('category')
            .filter(category__menu_type__ncode='300')
            .order_by('category__order', 'name')
        )