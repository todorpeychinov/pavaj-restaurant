from django.contrib import admin
from django.utils.html import format_html

from bookings.models import Booking


# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone_number',
        'date',
        'time',
        'guests',
        'colored_status',
        'is_email_sent',
        'confirmed_by',
        'created_at'
    )

    search_fields = (
        'full_name',
        'email',
        'phone_number',
        'user__username',
        'confirmed_by__username'
    )

    list_filter = (
        'status',
        'is_email_sent',
        'date',
        ('confirmed_by', admin.RelatedOnlyFieldListFilter),
    )

    ordering = ('-date', '-time', '-guests')

    fieldsets = (
        ('Customer Information', {
            'fields': ('user', 'full_name', 'email', 'phone_number')
        }),
        ('Booking Details', {
            'fields': ('date', 'time', 'guests', 'additional_info')
        }),
        ('Status & Management', {
            'fields': ('status', 'confirmed_by', 'is_email_sent')
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at'),
        }),
    )

    readonly_fields = ('created_at', 'updated_at', 'confirmed_by', )

    @admin.display(description="Status")
    def colored_status(self, obj):
        color_map = {
            'pending': 'orange',
            'confirmed': 'green',
            'rejected': 'red',
        }
        color = color_map.get(obj.status, 'gray')
        return format_html(f'<b><span style="color:{color}">{obj.status.capitalize()}</span></b>')


