from django import forms

from menu.models import Allergen, MenuItem, MenuCategory, MenuType


class AllergenBaseForm(forms.ModelForm):
    class Meta:
        model = Allergen
        fields = ['name', 'icon', 'ncode']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'add-allergen-textinput1 thq-input thq-body-large',
                'placeholder': 'Allergen'
            }),
            'icon': forms.URLInput(attrs={
                'class': 'add-allergen-textinput2 thq-input thq-body-large',
                'placeholder': 'Enter icon URL (optional)'
            }),
            'ncode': forms.NumberInput(attrs={
                'class': 'add-allergen-textinput3 thq-input thq-body-large',
                'placeholder': 'Enter unique code...'
            }),
        }


class AllergenCreateForm(AllergenBaseForm):
    ...


class AllergenEditForm(AllergenBaseForm):
    class Meta(AllergenBaseForm.Meta):
        fields = ['name', 'icon']


class MenuItemBaseForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = [
            'name', 'category', 'description', 'weight',
            'is_vegan', 'is_vegetarian', 'is_gluten_free', 'allergens'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'add-a-meal-textinput1 thq-input thq-body-large',
                'placeholder': 'Enter meal name...'
            }),
            'category': forms.Select(attrs={
                'class': 'thq-input thq-body-large',
                'placeholder': 'Select category...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'add-a-meal-textarea textarea',
                'rows': 3,
                'placeholder': 'Write a short description...'
            }),
            'weight': forms.NumberInput(attrs={
                'class': 'add-a-meal-textinput2 thq-input thq-body-large',
                'placeholder': 'Enter weight (grams)...'
            }),
            'allergens': forms.SelectMultiple(attrs={
                'class': 'thq-input thq-body-large',
                'size': 6,
                'style': 'width:100%; min-height:150px;',
            }),
        }


class MenuItemCreateForm(MenuItemBaseForm):
    ...


class MenuItemEditForm(MenuItemBaseForm):
    ...


class MenuCategoryBaseForm(forms.ModelForm):
    class Meta:
        model = MenuCategory
        fields = ['name', 'menu_type', 'description', 'ncode', 'order']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'add-menu-category-textinput1 thq-input thq-body-large',
                'placeholder': 'Enter menu category name...'
            }),
            'menu_type': forms.Select(attrs={
                'class': 'thq-input thq-body-large',
            }),
            'description': forms.Textarea(attrs={
                'class': 'add-menu-category-textarea textarea',
                'rows': 3,
                'placeholder': 'Enter menu category description (optional)...'
            }),
            'ncode': forms.NumberInput(attrs={
                'class': 'add-menu-category-textinput2 thq-input thq-body-large',
                'placeholder': 'Enter unique code...'
            }),
            'order': forms.NumberInput(attrs={
                'class': 'add-menu-category-textinput3 thq-input thq-body-large',
                'placeholder': 'Choose the order of this category in the menu...'
            }),
        }


class MenuCategoryCreateForm(MenuCategoryBaseForm):
    ...


class MenuCategoryEditForm(MenuCategoryBaseForm):
    class Meta(MenuCategoryBaseForm.Meta):
        fields = ['name', 'menu_type', 'description', 'order']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'edit-menu-category-textinput1 thq-input thq-body-large',
                'placeholder': 'Enter category name...'
            }),
            'menu_type': forms.Select(attrs={
                'class': 'thq-input thq-body-large',
            }),
            'description': forms.Textarea(attrs={
                'class': 'edit-menu-category-textarea textarea',
                'rows': 3,
                'placeholder': 'Enter description (optional)...'
            }),
            'order': forms.NumberInput(attrs={
                'class': 'edit-menu-category-textinput2 thq-input thq-body-large',
                'placeholder': 'Enter order number...'
            }),
        }


class MenuTypeBaseForm(forms.ModelForm):
    class Meta:
        model = MenuType
        fields = ['name', 'description', 'ncode']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'add-menu-type-textinput1 thq-input thq-body-large',
                'placeholder': 'Enter menu type name...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'add-menu-type-textarea textarea',
                'rows': 3,
                'placeholder': 'Enter menu type description (optional)...'
            }),
            'ncode': forms.NumberInput(attrs={
                'class': 'add-menu-type-textinput2 thq-input thq-body-large',
                'placeholder': 'Enter unique code...'
            }),
        }


class MenuTypeCreateForm(MenuTypeBaseForm):
    ...


class MenuTypeEditForm(MenuTypeBaseForm):
    class Meta(MenuTypeBaseForm.Meta):
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'add-menu-type-textinput1 thq-input thq-body-large',
                'placeholder': 'Enter menu type name...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'edit-menu-type-textarea thq-input thq-body-large',
                'rows': 3,
                'style': 'resize:none;',
                'placeholder': 'Enter menu type description (optional)...'
            }),
        }