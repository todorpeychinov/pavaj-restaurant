from rest_framework import serializers

from menu.models import Allergen, MenuItem, MenuCategory, MenuType


class AllergenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergen
        fields = ['name', 'icon']


class MenuItemSerializer(serializers.ModelSerializer):
    allergens = AllergenSerializer(many=True)

    class Meta:
        model = MenuItem
        fields = [
            'name',
            'description',
            'is_vegan',
            'is_vegetarian',
            'is_gluten_free',
            'weight',
            'allergens'
        ]


class MenuCategorySerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True)

    class Meta:
        model = MenuCategory
        fields = ['name', 'description', 'order', 'items']


class MenuTypeSerializer(serializers.ModelSerializer):
    categories = MenuCategorySerializer(many=True)

    class Meta:
        model = MenuType
        fields = ['name', 'description', 'categories']
