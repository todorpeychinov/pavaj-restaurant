from django.urls import path, include

from menu import views

urlpatterns = [
    path('allergens/', include([
        path('add-allergen/', views.AddAllergenView.as_view(), name='add-allergen'),
        path('allergens-list/', views.AllergensListView.as_view(), name='allergens'),
        path('<int:pk>/', include([
            path('edit-allergen/', views.EditAllergenView.as_view(), name='edit-allergen'),
            path('delete-allergen/', views.DeleteAllergenView.as_view(), name='delete-allergen'),
        ]))
    ])),

    path('menu-items/', include([
        path('add-menu-item/', views.AddMenuItemView.as_view(), name='add-menu-item'),
        path('menu-items-list/', views.MenuItemsListView.as_view(), name='menu-items'),
        path('<int:pk>/', include([
            path('edit-menu-item/', views.EditMenuItemView.as_view(), name='edit-menu-item'),
            path('delete-menu-item/', views.DeleteMenuItemView.as_view(), name='delete-menu-item'),
        ])),
    ])),

    path('menu-categories/', include([
        path('add-menu-category/', views.AddMenuCategoryView.as_view(), name='add-menu-category'),
        path('menu-categories-list/', views.MenuCategoriesListView.as_view(), name='menu-categories'),
        path('<int:pk>/', include([
            path('edit-menu-category/', views.EditMenuCategoryView.as_view(), name='edit-menu-category'),
            path('delete-menu-category/', views.DeleteMenuCategoryView.as_view(), name='delete-menu-category'),
        ]))
    ])),

    path('menu-types/', include([
        path('add-menu-type/', views.AddMenuTypeView.as_view(), name='add-menu-type'),
        path('menu-types-list/', views.MenuTypesListView.as_view(), name='menu-types'),
        path('<int:pk>/', include([
            path('edit-menu-type/', views.EditMenuTypeView.as_view(), name='edit-menu-type'),
            path('delete-menu-type/', views.DeleteMenuTypeView.as_view(), name='delete-menu-type'),
        ]))
    ])),
]
