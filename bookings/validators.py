import datetime

from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_booking_hour(value):
    if value < datetime.time(12, 0) or value > datetime.time(22, 0):
        raise ValidationError("Reservations are allowed only between 12:00 and 22:00.")


def validate_future_date(value):
    today = timezone.localdate()
    if value < today:
        raise ValidationError("The date cannot be in the past.")
