from django.db import models


class InquiryStatusChoices(models.TextChoices):
    IN_PROGRESS = 'in progress', 'in progress'
    RESOLVED = 'resolved', 'resolved'
