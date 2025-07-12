from django.urls import path

from menu import views

urlpatterns = [
    path('add-allergen/', views.add_allergen, name='add-allergen'),
    path('add-menu-item/', views.add_menu_item, name='add-menu-item'),
    path('add-menu-category/', views.add_menu_category, name='add-menu-category'),
    path('add-menu-type/', views.add_menu_type, name='add-menu-type'),
    path('allergens/', views.allergens, name='allergens'),
    path('edit-allergen/', views.edit_allergen, name='edit-allergen'),
    path('edit-menu-category/', views.edit_menu_category, name='edit-menu-category'),
    path('edit-menu-item/', views.edit_menu_item, name='edit-menu-item'),
    path('edit-menu-type/', views.edit_menu_type, name='edit-menu-type'),
    path('menu-categories/', views.menu_categories, name='menu-categories'),
    path('menu-items/', views.menu_items, name='menu-items'),
    path('menu-types/', views.menu_types, name='menu-types'),
]
