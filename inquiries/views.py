from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView, DetailView, TemplateView

from inquiries.choices import InquiryStatusChoices
from inquiries.forms import InquiryCreateForm, InquiryResponseForm
from inquiries.models import Inquiry

from core.tasks import send_async_email


# Create your views here.


class InquiryCreateView(LoginRequiredMixin, CreateView):
    model = Inquiry
    form_class = InquiryCreateForm
    template_name = "inquiries/sent-inquiry.html"
    success_url = reverse_lazy('thank-you')

    def get_initial(self):
        initial = super().get_initial()
        user = self.request.user
        if user.is_authenticated:
            full_name = f"{user.first_name} {user.last_name}".strip()
            initial['full_name'] = full_name if full_name else ''
            initial['email'] = user.email
            if hasattr(user, 'profile'):
                initial['phone_number'] = user.profile.phone_number or ''
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        try:
            send_async_email.delay(
                "Thank you for your inquiry",
                f"Hello {self.object.full_name},\n\n"
                f"Thank you for reaching out to us. We will respond as soon as possible.\n\n"
                f"Best regards,\nPavaj Restaurant",
                [self.object.email]
            )
        except Exception as e:
            print(f"Email sending failed: {e}")

        try:
            send_async_email.delay(
                "New Inquiry Received",
                f"New inquiry:\n\n"
                f"Name: {self.object.full_name}\n"
                f"Email: {self.object.email}\n"
                f"Phone Number: {self.object.phone_number}\n"
                f"Message: {self.object.message}\n\n",
                [settings.DEFAULT_FROM_EMAIL]
            )
        except Exception as e:
            print(f"Email sending failed: {e}")

        return super().form_valid(form)


class InquiriesListView(PermissionRequiredMixin, ListView):
    model = Inquiry
    template_name = "inquiries/inquiries-page.html"
    context_object_name = "inquiries"
    paginate_by = 3
    permission_required = "inquiries.can_manage_inquiries"

    def get_queryset(self):
        status = self.request.GET.get('status', InquiryStatusChoices.IN_PROGRESS)
        queryset = Inquiry.objects.all().order_by('-created_at')
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_status'] = self.request.GET.get('status', InquiryStatusChoices.IN_PROGRESS)
        context['statuses'] = InquiryStatusChoices.choices
        return context


class InquiryDetailView(PermissionRequiredMixin, DetailView):
    model = Inquiry
    template_name = "inquiries/inquiry-details.html"
    context_object_name = "inquiry"
    permission_required = "inquiries.can_manage_inquiries"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = InquiryStatusChoices
        context['responses'] = self.object.responses.all()
        return context


class InquiryAnswerView(PermissionRequiredMixin, FormView):
    template_name = "inquiries/answer-inquiry-page.html"
    form_class = InquiryResponseForm
    permission_required = "inquiries.can_manage_inquiries"

    def dispatch(self, request, *args, **kwargs):
        self.inquiry = get_object_or_404(Inquiry, pk=self.kwargs['pk'])

        if self.inquiry.status == InquiryStatusChoices.RESOLVED:
            messages.warning(request, "This inquiry has already been answered.")
            return redirect('inquiries-list')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inquiry'] = get_object_or_404(Inquiry, pk=self.kwargs['pk'])
        context['status_choices'] = InquiryStatusChoices
        return context

    def form_valid(self, form):
        inquiry = get_object_or_404(Inquiry, pk=self.kwargs['pk'])
        response = form.save(commit=False)
        response.inquiry = inquiry
        response.responder = self.request.user
        response.save()

        inquiry.status = InquiryStatusChoices.RESOLVED
        inquiry.responded_by = self.request.user

        try:
            send_async_email.delay(
                "Response to Your Inquiry",
                f"Hello {inquiry.full_name},\n\n"
                f"Our response:\n\n"
                f"{response.message}\n\n"
                f"Best regards,\nPavaj Restaurant",
                [inquiry.email]
            )
        except Exception as e:
            print(f"Email sending failed: {e}")

        inquiry.sent_email = True
        inquiry.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('inquiries-list')


class InquiryThankYouView(TemplateView):
    template_name = "inquiries/thank-you-page.html"
