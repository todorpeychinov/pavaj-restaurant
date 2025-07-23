from django.contrib import admin

from inquiries.models import Inquiry, InquiryResponse


# Register your models here.
@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    ...


@admin.register(InquiryResponse)
class InquiryResponseAdmin(admin.ModelAdmin):
    ...
