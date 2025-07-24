from django.contrib import admin
from django.utils.html import format_html

from menu.models import MenuType, MenuCategory, Allergen, MenuItem


# Register your models here.


class MenuCategoryInline(admin.TabularInline):
    model = MenuCategory
    extra = 0
    fields = ('name', 'order', 'ncode')
    ordering = ('order',)
    show_change_link = True


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 0
    fields = ('name', 'is_vegan', 'is_vegetarian', 'is_gluten_free', 'weight')
    show_change_link = True
    ordering = ('name',)


@admin.register(MenuType)
class MenuTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'ncode', 'description', 'created_at', 'last_time_edited')
    search_fields = ('name', 'description', 'ncode')
    ordering = ('name',)
    fieldsets = (
        ('General Information', {
            'fields': ('name', 'description', 'ncode')
        }),
        ('System Information', {
            'fields': ('created_at', 'last_time_edited', 'user_created', 'last_user_edited')
        }),
    )
    readonly_fields = ('created_at', 'last_time_edited', 'user_created', 'last_user_edited')
    inlines = [MenuCategoryInline]


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu_type', 'order', 'ncode', 'description', 'created_at')
    list_editable = ('order',)
    list_filter = ('menu_type',)
    search_fields = ('name', 'description', 'ncode', 'menu_type__name')
    ordering = ('menu_type__name', 'order')
    fieldsets = (
        ('General Information', {
            'fields': ('menu_type', 'name', 'description', 'ncode', 'order')
        }),
        ('System Information', {
            'fields': ('created_at', 'last_time_edited', 'user_created', 'last_user_edited')
        }),
    )
    readonly_fields = ('created_at', 'last_time_edited', 'user_created', 'last_user_edited')
    inlines = [MenuItemInline]


@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
    list_display = ('name', 'ncode', 'icon_preview', 'created_at')
    search_fields = ('name', 'ncode')
    ordering = ('name',)
    fieldsets = (
        ('General Information', {
            'fields': ('name', 'ncode', 'icon')
        }),
        ('System Information', {
            'fields': ('created_at', 'last_time_edited', 'user_created', 'last_user_edited', 'icon_preview')
        }),
    )
    readonly_fields = ('created_at', 'last_time_edited', 'user_created', 'last_user_edited', 'icon_preview')

    @admin.display(description="Icon")
    def icon_preview(self, obj):
        if obj.icon:
            return format_html(f'<img src="{obj.icon}" width="30" height="30" style="object-fit:cover;"/>')
        return "-"


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'is_vegan',
        'is_vegetarian',
        'is_gluten_free',
        'weight',
        'allergens_list',
        'created_at'
    )
    list_filter = ('category', 'is_vegan', 'is_vegetarian', 'is_gluten_free', 'allergens')
    search_fields = ('name', 'description', 'category__name', 'allergens__name')
    ordering = ('category__menu_type__name', 'name')
    filter_horizontal = ('allergens',)
    fieldsets = (
        ('General Information', {
            'fields': ('category', 'name', 'description', 'weight', 'allergens')
        }),
        ('Dietary Information', {
            'fields': ('is_vegan', 'is_vegetarian', 'is_gluten_free')
        }),
        ('System Information', {
            'fields': ('created_at', 'last_time_edited', 'user_created', 'last_user_edited')
        }),
    )
    readonly_fields = ('created_at', 'last_time_edited', 'user_created', 'last_user_edited')

    @admin.display(description="Allergens")
    def allergens_list(self, obj):
        return ", ".join([a.name for a in obj.allergens.all()]) if obj.allergens.exists() else "-"
