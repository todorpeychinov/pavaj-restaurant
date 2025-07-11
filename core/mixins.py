from django.contrib.auth import get_user_model
from django.db import models
from simple_history.models import HistoricalRecords

UserModel = get_user_model()


class TimeStampedUserTrackedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_time_edited = models.DateTimeField(auto_now=True)

    user_created = models.ForeignKey(
        UserModel,
        related_name="created_%(class)s_set",
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    last_user_edited = models.ForeignKey(
        UserModel,
        related_name="edited_%(class)s_set",
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    class Meta:
        abstract = True


class HistoryMixin(models.Model):
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
