from django.db import models

from core.mixins import TimeStampedUserTrackedModel, HistoryMixin


# Create your models here.

class MenuType(TimeStampedUserTrackedModel, HistoryMixin):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    ncode = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.name


class MenuCategory(TimeStampedUserTrackedModel, HistoryMixin):
    name = models.CharField(max_length=100)
    menu_type = models.ForeignKey(MenuType, on_delete=models.CASCADE, related_name='categories')
    description = models.TextField(blank=True, null=True)
    ncode = models.PositiveIntegerField(unique=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = (('name', 'menu_type'),)
        ordering = ('order',)

    def __str__(self):
        return f"{self.menu_type.name} – {self.name}"


class Allergen(TimeStampedUserTrackedModel, HistoryMixin):
    name = models.CharField(max_length=100)
    ncode = models.PositiveIntegerField(unique=True)
    icon = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class MenuItem(TimeStampedUserTrackedModel, HistoryMixin):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_vegan = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    weight = models.PositiveIntegerField(default=0)
    allergens = models.ManyToManyField(Allergen, blank=True)

