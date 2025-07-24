from django.contrib import admin

from accounts.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_email', 'phone_number')
    search_fields = ('user__username', 'user__email', 'phone_number')
    list_filter = ('user__is_active', 'user__is_staff')
    ordering = ('user__username',)
    fieldsets = (
        ('Main information', {
            'fields': ('user', 'phone_number'),
        }),
    )

    @admin.display(ordering='user__username', description='Username')
    def get_username(self, obj):
        return obj.user.username

    @admin.display(ordering='user__email', description='Email')
    def get_email(self, obj):
        return obj.user.email
