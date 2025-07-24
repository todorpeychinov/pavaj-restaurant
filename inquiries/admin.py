from django.contrib import admin
from django.utils.html import format_html

from inquiries.models import Inquiry, InquiryResponse


# Register your models here.
class InquiryResponseInline(admin.TabularInline):
    model = InquiryResponse
    extra = 0
    readonly_fields = ('responder', 'message', 'created_at')
    can_delete = False
    show_change_link = True


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'subject',
        'colored_status',
        'sent_email',
        'responded_by',
        'created_at'
    )

    search_fields = (
        'full_name',
        'email',
        'phone_number',
        'subject',
        'message',
        'user__username',
        'responded_by__username'
    )

    list_filter = (
        'status',
        'sent_email',
        'created_at',
        ('responded_by', admin.RelatedOnlyFieldListFilter),
    )

    ordering = ('-created_at',)

    fieldsets = (
        ('Customer Information', {
            'fields': ('user', 'full_name', 'email', 'phone_number')
        }),
        ('Inquiry Details', {
            'fields': ('subject', 'message')
        }),
        ('Status & Management', {
            'fields': ('status', 'responded_by', 'sent_email')
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at'),
        }),
    )

    readonly_fields = ('created_at', 'updated_at', 'subject', 'message', 'responded_by')

    inlines = [InquiryResponseInline]

    @admin.display(description="Status")
    def colored_status(self, obj):
        color_map = {
            'in progress': 'orange',
            'resolved': 'green',
        }
        color = color_map.get(obj.status, 'black')
        return format_html(f'<b><span style="color:{color}">{obj.status.capitalize()}</span></b>')


@admin.register(InquiryResponse)
class InquiryResponseAdmin(admin.ModelAdmin):
    list_display = ('responder', 'inquiry', 'short_message', 'created_at')
    search_fields = ('responder__username', 'inquiry__full_name', 'message')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    readonly_fields = ('created_at', 'message', 'responder', 'inquiry')

    @admin.display(description="Message")
    def short_message(self, obj):
        return (obj.message[:50] + "...") if len(obj.message) > 50 else obj.message
