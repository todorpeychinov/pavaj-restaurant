from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from menu.forms import AllergenCreateForm, MenuItemCreateForm, MenuCategoryCreateForm, MenuTypeCreateForm, \
    AllergenEditForm, MenuCategoryEditForm, MenuItemEditForm, MenuTypeEditForm
from menu.mixins import UserTrackedMixin
from menu.models import Allergen, MenuItem, MenuCategory, MenuType


# Create your views here.
class AddAllergenView(UserTrackedMixin, PermissionRequiredMixin, CreateView):
    model = Allergen
    form_class = AllergenCreateForm
    template_name = "menu/add-allergen-page.html"
    success_url = reverse_lazy('allergens')
    permission_required = "menu.can_manage_menu"


class AddMenuItemView(UserTrackedMixin, PermissionRequiredMixin, CreateView):
    model = MenuItem
    form_class = MenuItemCreateForm
    template_name = "menu/add-item-to-menu.html"
    success_url = reverse_lazy('menu-items')
    permission_required = "menu.can_manage_menu"


class AddMenuCategoryView(UserTrackedMixin, PermissionRequiredMixin, CreateView):
    model = MenuCategory
    form_class = MenuCategoryCreateForm
    template_name = "menu/add-menu-category-page.html"
    success_url = reverse_lazy('menu-categories')
    permission_required = "menu.can_manage_menu"


class AddMenuTypeView(UserTrackedMixin, PermissionRequiredMixin, CreateView):
    model = MenuType
    form_class = MenuTypeCreateForm
    template_name = "menu/add-menu-type-page.html"
    success_url = reverse_lazy('menu-types')
    permission_required = "menu.can_manage_menu"


class AllergensListView(PermissionRequiredMixin, ListView):
    model = Allergen
    template_name = "menu/allergens-page.html"
    context_object_name = "allergens"
    permission_required = "menu.can_manage_menu"
    paginate_by = 7

    def get_queryset(self):
        return Allergen.objects.all().order_by('ncode')


class MenuCategoriesListView(PermissionRequiredMixin, ListView):
    model = MenuCategory
    template_name = "menu/menu-categories-page.html"
    context_object_name = "categories"
    permission_required = "menu.can_manage_menu"
    paginate_by = 5

    def get_queryset(self):
        return MenuCategory.objects.all().order_by('menu_type', 'ncode')


class MenuItemsListView(PermissionRequiredMixin, ListView):
    model = MenuItem
    template_name = "menu/menu-items-page.html"
    context_object_name = "items"
    permission_required = "menu.can_manage_menu"
    paginate_by = 5

    def get_queryset(self):
        return MenuItem.objects.all().order_by('category__menu_type', 'category')


class MenuTypesListView(PermissionRequiredMixin, ListView):
    model = MenuType
    template_name = "menu/menu-types-page.html"
    context_object_name = "types"
    permission_required = "menu.can_manage_menu"
    paginate_by = 7

    def get_queryset(self):
        return MenuType.objects.all().order_by('ncode')


class EditAllergenView(UserTrackedMixin, PermissionRequiredMixin, UpdateView):
    model = Allergen
    form_class = AllergenEditForm
    template_name = "menu/edit-allergen-page.html"
    success_url = reverse_lazy('allergens')
    permission_required = "menu.can_manage_menu"


class EditMenuCategoryView(UserTrackedMixin, PermissionRequiredMixin, UpdateView):
    model = MenuCategory
    form_class = MenuCategoryEditForm
    template_name = "menu/edit-menu-category-page.html"
    success_url = reverse_lazy('menu-categories')
    permission_required = "menu.can_manage_menu"


class EditMenuItemView(UserTrackedMixin, PermissionRequiredMixin, UpdateView):
    model = MenuItem
    form_class = MenuItemEditForm
    template_name = "menu/edit-menu-item.html"
    success_url = reverse_lazy('menu-items')
    permission_required = "menu.can_manage_menu"


class EditMenuTypeView(UserTrackedMixin, PermissionRequiredMixin, UpdateView):
    model = MenuType
    form_class = MenuTypeEditForm
    template_name = "menu/edit-menu-type-page.html"
    success_url = reverse_lazy('menu-types')
    permission_required = "menu.can_manage_menu"


class DeleteAllergenView(PermissionRequiredMixin, DeleteView):
    model = Allergen
    template_name = "menu/delete-confirmation-page-allergen.html"
    success_url = reverse_lazy('allergens')
    permission_required = "menu.can_manage_menu"


class DeleteMenuCategoryView(PermissionRequiredMixin, DeleteView):
    model = MenuCategory
    template_name = "menu/delete-confirmation-page-category.html"
    success_url = reverse_lazy('menu-categories')
    permission_required = "menu.can_manage_menu"


class DeleteMenuItemView(PermissionRequiredMixin, DeleteView):
    model = MenuItem
    template_name = "menu/delete-confirmation-page-menu-item.html"
    success_url = reverse_lazy('menu-items')
    permission_required = "menu.can_manage_menu"


class DeleteMenuTypeView(PermissionRequiredMixin, DeleteView):
    model = MenuType
    template_name = "menu/delete-confirmation-page-menu-type.html"
    success_url = reverse_lazy('menu-types')
    permission_required = "menu.can_manage_menu"
