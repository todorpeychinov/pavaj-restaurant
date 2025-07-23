from django.contrib.auth import get_user_model
from django.db import models

from core.mixins import HistoryMixin
from inquiries.choices import InquiryStatusChoices

# Create your models here.

UserModel = get_user_model()


class Inquiry(HistoryMixin):

    user = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='inquiries'
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=150, blank=True)
    message = models.TextField()

    status = models.CharField(max_length=20, choices=InquiryStatusChoices.choices, default='in progress')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    responded_by = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='responded_inquiries'
    )

    sent_email = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        permissions = [
            ("can_manage_inquiries", "Can view and respond to inquiries")
        ]

    def __str__(self):
        return f"Inquiry from {self.full_name} – {self.status}"


class InquiryResponse(HistoryMixin):
    inquiry = models.ForeignKey(
        Inquiry,
        on_delete=models.CASCADE,
        related_name='responses'
    )
    responder = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='inquiry_responses'
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Response to {self.inquiry.full_name} by {self.responder} on {self.created_at:%Y-%m-%d}"


