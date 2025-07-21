from django import forms

from bookings.models import Booking


class BookingBaseForm(forms.ModelForm):
    confirm_policy = forms.BooleanField(
        required=True,
        label="I confirm that I have read and agree to the Privacy Policy and Data Protection Terms."
    )

    class Meta:
        model = Booking
        exclude = ['user', 'status', 'created_at', 'updated_at', 'confirmed_by', 'is_email_sent']
        widgets = {
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'min': '12:00',
                'max': '22:00',
                'class': 'booking-form-textinput5 thq-input thq-body-large'
            }),
        }


class BookingCreateForm(BookingBaseForm):
    ...