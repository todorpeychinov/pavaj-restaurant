from django import forms

from inquiries.models import Inquiry, InquiryResponse


class InquiryBaseForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        exclude = ['user', 'status', 'created_at', 'updated_at', 'responded_by', 'sent_email']


class InquiryCreateForm(InquiryBaseForm):
    confirm_policy = forms.BooleanField(
        required=True,
        label="I confirm that I have read and agree to the Privacy Policy and Data Protection Terms.",
        error_messages={
            'required': 'You must agree to the Privacy Policy and Data Protection Terms in order to proceed.'
        },
    )


class InquiryBaseForm(forms.ModelForm):
    class Meta:
        model = InquiryResponse
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter your message here...'})
        }


class InquiryResponseForm(InquiryBaseForm):
    ...
