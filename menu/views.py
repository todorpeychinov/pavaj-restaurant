from django.shortcuts import render


# Create your views here.


def add_allergen(request):
    return render(request, 'menu/add-allergen-page.html')


def add_menu_item(request):
    return render(request, 'menu/add-item-to-menu.html')


def add_menu_category(request):
    return render(request, 'menu/add-menu-category-page.html')


def add_menu_type(request):
    return render(request, 'menu/add-menu-type-page.html')


def allergens(request):
    return render(request, 'menu/allergens-page.html')


def edit_allergen(request):
    return render(request, 'menu/edit-allergen-page.html')


def edit_menu_category(request):
    return render(request, 'menu/edit-menu-category-page.html')


def edit_menu_item(request):
    return render(request, 'menu/edit-menu-item.html')


def edit_menu_type(request):
    return render(request, 'menu/edit-menu-type-page.html')


def menu_categories(request):
    return render(request, 'menu/menu-categories-page.html')


def menu_items(request):
    return render(request, 'menu/menu-items-page.html')


def menu_types(request):
    return render(request, 'menu/menu-types-page.html')
