from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.timezone import now
from django.views.generic import FormView, DetailView, ListView, UpdateView

from bookings.choices import ReservationStatusChoices
from bookings.forms import BookingCreateForm, BookingEditForm
from bookings.models import Booking
from core.tasks import send_async_email


# Create your views here.
class BookATableView(LoginRequiredMixin, FormView):
    template_name = "bookings/book-a-table.html"
    form_class = BookingCreateForm
    success_url = reverse_lazy('client-bookings')

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
                "Reservation Request Received",
                f"Hello {self.object.full_name},\n\n"
                f"Thank you for your reservation request.\n"
                f"We will confirm or reject it shortly.\n\n"
                f"Best regards,\nPavaj Restaurant",
                [self.object.email]
            )
        except Exception as e:
            print(f"Email sending failed: {e}")

        try:
            send_async_email.delay(
                "New Reservation Request Received",
                f"A new reservation request has been received:\n\n"
                f"Name: {self.object.full_name}\n"
                f"Email: {self.object.email}\n"
                f"Phone: {self.object.phone_number}\n"
                f"Date: {self.object.date}\n"
                f"Time: {self.object.time}\n"
                f"Guests: {self.object.guests}\n"
                f"Additional Info: {self.object.additional_info or 'N/A'}\n\n"
                f"Please review the reservation in the management panel.",
                [settings.DEFAULT_FROM_EMAIL]
            )
        except Exception as e:
            print(f"Email sending failed: {e}")

        return super().form_valid(form)


class BookingDetailsView(PermissionRequiredMixin, DetailView):
    template_name = 'bookings/booking-details.html'
    model = Booking
    permission_required = "bookings.can_manage_bookings"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STATUS'] = ReservationStatusChoices
        return context


@permission_required('bookings.can_manage_bookings')
def confirm_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, status=ReservationStatusChoices.PENDING)
    booking.status = ReservationStatusChoices.CONFIRMED
    booking.confirmed_by = request.user

    try:
        send_async_email.delay(
            "Reservation Confirmed",
            f"Hello {booking.full_name},\n\n"
            f"Your reservation for {booking.date} at {booking.time} has been confirmed.\n\n"
            f"Best regards,\nPavaj Restaurant",
            [booking.email]
        )
    except Exception as e:
        print(f"Email sending failed: {e}")

    booking.is_email_sent = True
    booking.save()

    status = request.GET.get('status', 'pending')
    page = request.GET.get('page', '1')
    return redirect(f"{reverse('bookings')}?status={status}&page={page}")


@permission_required('bookings.can_manage_bookings')
def reject_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, status=ReservationStatusChoices.PENDING)
    booking.status = ReservationStatusChoices.REJECTED
    booking.confirmed_by = request.user

    try:
        send_async_email.delay(
            "Reservation Rejected",
            f"Hello {booking.full_name},\n\n"
            f"Unfortunately, we cannot confirm your reservation for {booking.date} at {booking.time}.\n\n"
            f"Best regards,\nPavaj Restaurant",
            [booking.email]
        )
    except Exception as e:
        print(f"Email sending failed: {e}")

    booking.is_email_sent = True
    booking.save()

    status = request.GET.get('status', 'pending')
    page = request.GET.get('page', '1')
    return redirect(f"{reverse('bookings')}?status={status}&page={page}")


class BookingsListView(PermissionRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/bookings.html'
    context_object_name = 'bookings'
    paginate_by = 3
    permission_required = "bookings.can_manage_bookings"

    def get_queryset(self):
        status = self.request.GET.get('status', ReservationStatusChoices.PENDING)
        return Booking.objects.filter(status=status, date__gte=now().date()).order_by('date', 'time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STATUS'] = ReservationStatusChoices
        context['statuses'] = ReservationStatusChoices.choices
        context['selected_status'] = self.request.GET.get('status', ReservationStatusChoices.PENDING)
        return context


class FutureBookingsClientView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/bookings-client.html'
    context_object_name = 'bookings'
    paginate_by = 3

    def get_queryset(self):
        return Booking.objects.filter(
            user=self.request.user,
            date__gte=now().date()
        ).order_by('date', 'time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STATUS'] = ReservationStatusChoices
        return context


@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    booking.status = ReservationStatusChoices.CANCELLED
    booking.save()

    try:
        send_async_email.delay(
            "Reservation Cancelled",
            f"Hello {booking.full_name},\n\n"
            f"Your reservation for {booking.date} at {booking.time} has been successfully cancelled.\n\n"
            f"If this was a mistake or you wish to make a new reservation, "
            f"feel free to contact us or book again through our website.\n\n"
            f"Best regards,\nPavaj Restaurant",
            [booking.email]
        )
    except Exception as e:
        print(f"Email sending failed: {e}")

    try:
        send_async_email.delay(
            "Reservation Cancelled by Customer",
            f"The following reservation has been cancelled by the customer:\n\n"
            f"Name: {booking.full_name}\n"
            f"Email: {booking.email}\n"
            f"Phone: {booking.phone_number}\n"
            f"Date: {booking.date}\n"
            f"Time: {booking.time}\n"
            f"Guests: {booking.guests}\n\n"
            f"No further action is required.",
            [settings.DEFAULT_FROM_EMAIL]
        )
    except Exception as e:
        print(f"Email sending failed: {e}")

    page = request.GET.get('page', '1')
    return redirect(f"{reverse('client-bookings')}?page={page}#booking-{pk}")


class BookingEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    form_class = BookingEditForm
    template_name = 'bookings/edit-booking.html'

    def get_success_url(self):
        return reverse_lazy('client-bookings')

    def test_func(self):
        return self.request.user == self.get_object().user and self.get_object().status == ReservationStatusChoices.PENDING
