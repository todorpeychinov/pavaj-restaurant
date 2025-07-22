from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxValueValidator
from django.db import models

from bookings.choices import ReservationStatusChoices
from bookings.validators import validate_booking_hour, validate_future_date
from core.mixins import HistoryMixin

# Create your models here.

UserModel = get_user_model()


class Booking(HistoryMixin):
    user = models.ForeignKey(
        UserModel, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='bookings'
    )
    full_name = models.CharField(
        max_length=100)  # тези полета са тук, ако в някакъв етап се направи възможна резервацията без акаунт
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    date = models.DateField(validators=[validate_future_date,])
    time = models.TimeField(validators=[validate_booking_hour,])
    guests = models.PositiveIntegerField()
    additional_info = models.TextField(blank=True)

    status = models.CharField(max_length=20, choices=ReservationStatusChoices.choices, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    confirmed_by = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='confirmed_bookings'
    )

    is_email_sent = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date', '-time']
        permissions = [
            ("can_manage_bookings", "Can confirm or reject bookings"),
        ]

    def __str__(self):
        return f"{self.full_name} – {self.date} @ {self.time} ({self.guests} guests)"


