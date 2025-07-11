from django.contrib import admin

from menu.models import MenuType, MenuCategory, Allergen, MenuItem


# Register your models here.
@admin.register(MenuType)
class MenuTypeAdmin(admin.ModelAdmin):
    ...


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
    ...

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    ...
